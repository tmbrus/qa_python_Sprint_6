import allure
from pages.header_footer_page import HeaderFooterPage


@allure.suite('Тестирование редиректов')
class TestRedirects:
    @allure.title('Проверка перехода по логотипу Яндекса')
    def test_yandex_logo_redirects_to_dzen(self, driver):
        """
        Проверка редиректа на Dzen при клике на логотип Яндекса
        Steps:
            1. Создаем экземпляр страницы
            2. Кликаем по логотипу Яндекса через метод страницы
            3. Проверяем переход на Dzen через методы страницы
        """
        # 1. Инициализируем page object
        header_footer_page = HeaderFooterPage(driver)

        # 2. Выполняем переход через метод страницы
        header_footer_page.go_to_yandex_from_logo()

        # 3. Проверяем результат через методы страницы
        assert header_footer_page.is_dzen_logo_displayed(), (
            "Логотип Dzen не отображается после перехода"
        )