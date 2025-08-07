import allure
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

    @allure.step('Переход по логотипу Яндекса и переключение на новую вкладку')
    def go_to_yandex_from_logo(self):
        """
        Переход на страницу Дзена по клику на логотип Яндекса: клик + ожидание новой вкладки + переключение

        Returns:
            str: URL открытой страницы Dzen
        """
        original_windows = self.get_windows_handles()
        self.click_to_element(HeaderFooterLocators.YANDEX_LOGO)
        new_window = self.wait_for_new_window(original_windows, timeout=15)
        self.switch_to_window(new_window)
        self.wait_for_url_contains("dzen.ru", timeout=15)

    @allure.step('Проверка наличия логотипа Дзена')
    def is_dzen_logo_displayed(self, timeout=10):
        """
        Проверка видимости логотипа Дзена на странице

        Args:
            timeout: Максимальное время ожидания в секундах (по умолчанию 10)

        Returns:
            bool: True если логотип видим, иначе False
        """
        from selenium.common.exceptions import TimeoutException
        try:
            return self.wait_for_element_visible(
                HeaderFooterLocators.DZEN_LOGO,
                timeout=timeout
            ).is_displayed()
        except TimeoutException:
            return False