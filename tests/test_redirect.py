import allure
from pages.header_footer_page import HeaderFooterPage


@allure.suite('Тестирование редиректов')
class TestRedirects:
    @allure.title('Проверка перехода по логотипу Яндекса')
    def test_yandex_logo_redirects_to_dzen(self, driver):
        """
        Проверка редиректа на Dzen при клике на логотип Яндекса

        Шаги:
        1. Клик по логотипу Яндекса через HeaderFooterPage
        2. Автоматическое ожидание и переключение на новую вкладку
        3. Проверка URL и видимости логотипа Dzen
        """
        header_footer_page = HeaderFooterPage(driver)

        # Выполняем переход (вся логика внутри Page Object)
        header_footer_page.go_to_yandex_from_logo()

        # Проверяем результат
        assert 'dzen.ru' in driver.current_url.lower(), (
            f"Не удалось перейти на Dzen. Текущий URL: {driver.current_url}")

        assert header_footer_page.is_dzen_logo_displayed(), (
            "Логотип Dzen не отображается на странице")