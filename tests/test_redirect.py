import allure
from pages.header_footer_page import HeaderFooterPage


@allure.suite('Тестирование редиректов')
class TestRedirects:
    @allure.title('Проверка перехода по логотипу Яндекса')
    def test_yandex_logo_redirects_to_dzen(self, driver):
        """
        Проверка редиректа на Dzen при клике на логотип Яндекса
        """
        header_footer_page = HeaderFooterPage(driver)
        header_footer_page.go_to_yandex_from_logo()
        assert header_footer_page.is_dzen_logo_displayed(), "Логотип Dzen не отображается"