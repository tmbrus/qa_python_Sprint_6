import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Базовый класс страницы с общими универсальными методами для работы с веб-элементами"""

    def __init__(self, driver):
        """Инициализация базовой страницы с драйвером браузера"""
        self.driver = driver

    @allure.step('Клик по элементу')
    def click_to_element(self, locator, timeout=20):
        """
        Выполняет клик по элементу с ожиданием его кликабельности

        Args:
            locator: Кортеж (By, локатор) для поиска элемента
            timeout: Максимальное время ожидания в секундах (по умолчанию 20)

        Raises:
            TimeoutException: Если элемент не становится кликабельным в течение указанного времени
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не стал кликабельным за {timeout} секунд"
        )
        element.click()

    @allure.step('Получение текста элемента')
    def get_element_text(self, locator, timeout=10):
        """
        Получает текст из видимого элемента

        Args:
            locator: Кортеж (By, локатор) для поиска элемента
            timeout: Максимальное время ожидания в секундах

        Returns:
            str: Текст элемента
        """
        element = self.wait_for_element_visible(locator, timeout)
        return element.text

    @staticmethod
    def format_locators(locator_template, num):
        """
        Форматирует локатор с подстановкой номера

        Args:
            locator_template: Шаблон локатора (method, locator)
            num: Номер для подстановки в локатор

        Returns:
            Кортеж: (method, formatted_locator)
        """
        method, locator = locator_template
        return method, locator.format(num)

    @property
    def current_url(self):
        """Возвращает текущий URL страницы"""
        return self.driver.current_url

    @allure.step('Заполнение поля')
    def fill_field(self, locator, value, timeout=10):
        """
        Заполняет поле указанным значением с явным ожиданием

        Args:
            locator: Кортеж (By, локатор) для поиска элемента
            value: Строка для ввода
            timeout: Максимальное время ожидания
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Не удалось найти элемент с локатором {locator}"
        )
        element.clear()
        element.send_keys(value)

    @allure.step('Прокрутка к элементу')
    def scroll_to_element(self, locator, timeout=10):
        """
        Прокручивает страницу до указанного элемента

        Args:
            locator: Кортеж (By, локатор) для поиска элемента
            timeout: Максимальное время ожидания
        """
        element = self.wait_for_element_visible(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Ожидание видимости элемента')
    def wait_for_element_visible(self, locator, timeout=10):
        """
        Ожидает появления и видимости элемента

        Args:
            locator: Кортеж (By, локатор) для поиска элемента
            timeout: Максимальное время ожидания в секундах

        Returns:
            WebElement: Найденный элемент
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не стал видимым за {timeout} секунд"
        )

    @allure.step('Получение списка открытых окон браузера')
    def get_windows_handles(self):
        """Возвращает список дескрипторов открытых окон браузера"""
        return self.driver.window_handles

    @allure.step('Ожидание появления новой вкладки')
    def wait_for_new_window(self, old_windows, timeout=10):
        """
        Ожидает появления новой вкладки, которой нет в списке old_windows

        Args:
            old_windows: Список дескрипторов окон до появления нового
            timeout: Максимальное время ожидания в секундах

        Returns:
            str: дескриптор новой вкладки
        """
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: [win for win in driver.window_handles if win not in old_windows][0],
            message=f"Новое окно не появилось за {timeout} секунд"
        )

    @allure.step('Переключение на окно')
    def switch_to_window(self, window_handle):
        """Переключается на указанное окно браузера"""
        self.driver.switch_to.window(window_handle)

    @allure.step('Ожидание загрузки страницы с URL содержащим подстроку')
    def wait_for_url_contains(self, substring, timeout=10):
        """
        Ожидает, что URL текущей страницы содержит указанную подстроку

        Args:
            substring: Подстрока, которая должна появиться в URL
            timeout: Максимальное время ожидания в секундах
        """
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(substring),
            message=f"URL не содержит подстроку '{substring}' за {timeout} секунд"
        )

    @allure.step('Проверка наличия элемента на странице')
    def is_element_present(self, locator, timeout=5):
        """
        Проверяет наличие элемента на странице

        Args:
            locator: Кортеж (By, локатор) для поиска элемента
            timeout: Максимальное время ожидания в секундах

        Returns:
            bool: True если элемент присутствует, False если нет
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except:
            return False

    @allure.step('Принять cookies')
    def accept_cookies(self, cookie_locator=(By.ID, 'rcc-confirm-button')):
        """
        Принимает cookies, если отображается кнопка

        Args:
            cookie_locator: Локатор кнопки принятия cookies
                           (по умолчанию (By.ID, 'rcc-confirm-button'))
        """
        if self.is_element_present(cookie_locator):
            self.click_to_element(cookie_locator)
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="cookies_accepted",
                attachment_type=allure.attachment_type.PNG
            )

    @allure.step('Сделать скриншот')
    def take_screenshot(self, name="screenshot"):
        """
        Делает скриншот текущей страницы и прикрепляет к отчету Allure

        Args:
            name: Имя для скриншота в отчете
        """
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step('Ожидание количества окон')
    def wait_for_number_of_windows(self, number, timeout=10):
        """
        Ожидает пока не откроется указанное количество окон
        Args:
            number: Ожидаемое количество окон
            timeout: Максимальное время ожидания
        """
        WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(number),
            message=f"Количество окон не стало равным {number} за {timeout} секунд"
        )

    @allure.step('Переключение на новое окно')
    def switch_to_new_window(self, main_window):
        """
        Переключается на новое окно (отличное от указанного)
        Args:
            main_window: Дескриптор исходного окна
        Returns:
            str: Дескриптор нового окна
        """
        new_window = [win for win in self.driver.window_handles if win != main_window][0]
        self.driver.switch_to.window(new_window)
        return new_window

    @allure.step('Проверка URL')
    def wait_for_url_contains_text(self, text, timeout=10):
        """
        Ожидает пока URL не будет содержать указанный текст
        Args:
            text: Текст который должен содержаться в URL
            timeout: Максимальное время ожидания
        """
        WebDriverWait(self.driver, timeout).until(
            lambda d: text.lower() in d.current_url.lower(),
            message=f"URL не содержит текст '{text}' за {timeout} секунд"
        )
