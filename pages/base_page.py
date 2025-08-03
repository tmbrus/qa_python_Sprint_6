import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.header_footer_locators import HeaderFooterLocators


class BasePage:
    """Базовый класс страницы, содержащий общие методы для работы с веб-элементами"""

    def __init__(self, driver):
        """Инициализация базовой страницы с драйвером браузера"""
        self.driver = driver

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        """
        Выполняет клик по указанному элементу с ожиданием его кликабельности

        Args:
            locator: Кортеж (By, локатор) для поиска элемента

        Raises:
            TimeoutException: Если элемент не становится кликабельным в течение 20 секунд
        """
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('Получение текста элемента')
    def get_element_text(self, locator):
        """
        Получает текст из видимого элемента

        Args:
            locator: Кортеж (By, локатор) для поиска элемента

        Returns:
            str: Текст элемента

        Raises:
            TimeoutException: Если элемент не становится видимым
        """
        element = self.wait_for_element_visible(locator)
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
        """Заполняет поле указанным значением с явным ожиданием"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Не удалось найти элемент с локатором {locator}"
        )
        element.clear()
        element.send_keys(value)

    @allure.step('Принятие куки-соглашения')
    def accept_cookies(self):
        """Принимает соглашение об использовании cookies, если кнопка доступна"""
        try:
            self.click_to_element(HeaderFooterLocators.COOKIE_BUTTON)
        except Exception as e:
            print(f"Cookie button not found or not clickable: {str(e)}")

    @allure.step('Прокрутка к элементу')
    def scroll_to_element(self, locator):
        """
        Прокручивает страницу до указанного элемента

        Args:
            locator: Кортеж (By, локатор) для поиска элемента
        """
        element = self.wait_for_element_visible(locator)
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

        Raises:
            TimeoutException: Если элемент не становится видимым в течение timeout
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент с локатором {locator} не стал видимым в течение {timeout} секунд."
        )

    @allure.step('Ожидание видимости группы элементов')
    def find_elements_with_wait(self, locator, timeout=10):
        """
        Ожидает появления и видимости всех элементов по локатору

        Args:
            locator: Кортеж (By, локатор) для поиска элементов
            timeout: Максимальное время ожидания в секундах

        Returns:
            List[WebElement]: Список найденных элементов

        Raises:
            TimeoutException: Если элементы не становятся видимыми в течение timeout
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator),
            message=f"Элементы с локатором {locator} не стали видимыми в течение {timeout} секунд."
        )

    @allure.step('Прокрутка страницы вниз')
    def scroll_to_bottom(self):
        """Прокручивает страницу до самого низа"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Переключение на вкладку браузера')
    def switch_to_tab(self, tab_index):
        """
        Переключает контекст на указанную вкладку браузера

        Args:
            tab_index: Индекс вкладки (0-based)
        """
        try:
            window_handles = self.driver.window_handles
            self.driver.switch_to.window(window_handles[tab_index])
        except Exception as e:
            print(f"Ошибка при переключении на вкладку {tab_index}: {str(e)}")

    @allure.step('Клик по элементу по тегу')
    def click_by_tag_name(self, tag_name):
        """
        Выполняет клик по первому найденному элементу с указанным тегом

        Args:
            tag_name: Название HTML-тега (например, 'body', 'div')
        """
        element = self.driver.find_element(By.TAG_NAME, tag_name)
        element.click()