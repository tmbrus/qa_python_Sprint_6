import allure
from pages.header_footer_page import HeaderFooterPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.suite('Тестирование редиректов')
class TestRedirects:
    @allure.title('Проверка перехода по логотипу Яндекса')
    def test_yandex_logo_redirects_to_dzen(self, driver):
        """
        Проверка редиректа на Dzen при клике на логотип Яндекса
        """
        header_footer_page = HeaderFooterPage(driver)

        # 1. Запоминаем текущее окно
        main_window = driver.current_window_handle

        # 2. Кликаем по логотипу Яндекса
        header_footer_page.go_to_yandex_from_logo()

        # 3. Ждем открытия нового окна и переключаемся на него
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
            if window_handle != main_window:
                driver.switch_to.window(window_handle)
                break

        # 4. Ждем загрузки страницы и проверяем URL
        WebDriverWait(driver, 15).until(
            lambda d: 'dzen.ru' in d.current_url.lower()
        )

        # 5. Проверяем что мы на Dzen
        assert 'dzen.ru' in driver.current_url.lower(), (
            f"Ожидался переход на Dzen, но текущий URL: {driver.current_url}"
        )