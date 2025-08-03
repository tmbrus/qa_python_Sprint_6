import allure
from selenium.webdriver.support.ui import WebDriverWait
from locators.header_footer_locators import HeaderFooterLocators
from pages.base_page import BasePage


class HeaderFooterPage(BasePage):
    """Класс для работы с элементами шапки и подвала страницы"""

    @allure.step('Клик по логотипу Самоката')
    def click_scooter_logo(self):
        """
        Переход на главную страницу по клику на логотип Самоката

        Returns:
            str: URL страницы после перехода
        """
        self.click_to_element(HeaderFooterLocators.SAMOKAT_LOGO)
        return self.current_url

    @allure.step('Переход по логотипу Яндекса')
    def go_to_yandex_from_logo(self):
        """
        Переход на страницу Дзена по клику на логотип Яндекса

        Returns:
            str: URL открытой страницы Dzen
        """
        # Запоминаем текущее окно и список окон до клика
        original_window = self.driver.current_window_handle
        windows_before = self.driver.window_handles

        # Кликаем по логотипу Яндекса
        self.click_to_element(HeaderFooterLocators.YANDEX_LOGO)

        # Ожидаем появления новой вкладки (15 секунд)
        WebDriverWait(self.driver, 15).until(
            lambda d: len(d.window_handles) > len(windows_before)
        )

        # Находим новую вкладку
        new_window = [x for x in self.driver.window_handles if x not in windows_before][0]
        self.driver.switch_to.window(new_window)

        # Ожидаем загрузки страницы Dzen (по домену)
        WebDriverWait(self.driver, 15).until(
            lambda d: 'dzen.ru' in d.current_url.lower()
        )

        return self.driver.current_url

    @allure.step('Проверка наличия логотипа Дзена')
    def is_dzen_logo_displayed(self, timeout=10):
        """
        Проверка видимости логотипа Дзена на странице

        Args:
            timeout: Максимальное время ожидания в секундах (по умолчанию 10)

        Returns:
            bool: True если логотип видим, иначе False
        """
        try:
            return self.wait_for_element_visible(
                HeaderFooterLocators.DZEN_LOGO,
                timeout=timeout
            ).is_displayed()
        except Exception:
            return False