import allure
from pages.header_footer_page import HeaderFooterPage
from pages.base_page import BasePage


@allure.suite('Тестирование редиректов')
class TestRedirects:
    @allure.title('Проверка перехода по логотипу Яндекса')
    def test_yandex_logo_redirects_to_dzen(self, driver):
        """
        Проверка редиректа на Dzen при клике на логотип Яндекса
        Steps:
            1. Запоминаем текущее окно
            2. Кликаем по логотипу Яндекса
            3. Ждем открытия нового окна и переключаемся на него
            4. Проверяем что мы на Dzen
        """
        header_footer_page = HeaderFooterPage(driver)
        base_page = BasePage(driver)

        # 1. Запоминаем текущее окно
        main_window = driver.current_window_handle

        # 2. Кликаем по логотипу Яндекса
        header_footer_page.go_to_yandex_from_logo()

        # 3. Ждем открытия нового окна и переключаемся на него
        base_page.wait_for_number_of_windows(2)
        base_page.switch_to_new_window(main_window)

        # 4. Проверяем что мы на Dzen
        base_page.wait_for_url_contains_text('dzen.ru')
        assert 'dzen.ru' in driver.current_url.lower(), (
            f"Ожидался переход на Dzen, но текущий URL: {driver.current_url}"
        )