import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """Класс для работы с главной страницей сервиса."""

    @allure.step('Принять cookies')
    def accept_cookies(self):
        """
        Принимает cookies на главной странице.
        Ожидает появления кнопки и кликает по ней.
        """
        self.wait_for_element_clickable(MainPageLocators.COOKIE_BUTTON, timeout=10)
        self.click_to_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Получить текст ответа для вопроса {index}')
    def get_answer_text(self, index: int) -> str:
        """
        Получает текст ответа на вопрос FAQ.

        Args:
            index: Номер вопроса (начиная с 0)

        Returns:
            Текст ответа

        Raises:
            ValueError: Если передан некорректный индекс
            TimeoutException: Если элементы не найдены
        """
        if not isinstance(index, int) or index < 0:
            raise ValueError("Индекс вопроса должен быть положительным целым числом")

        # Получаем и кликаем по вопросу
        question = self._get_question_element(index)
        self._click_question(question, index)

        # Получаем и возвращаем текст ответа
        return self._get_answer_text(index)

    @allure.step('Найти вопрос {index}')
    def _get_question_element(self, index: int):
        """Находит и возвращает элемент вопроса по индексу."""
        locator = self.format_locator(MainPageLocators.QUESTION_TEMPLATE, index)
        self.scroll_to_element(locator)
        return self.wait_for_element_visible(locator, timeout=15)

    @allure.step('Кликнуть по вопросу')
    def _click_question(self, question_element, index):
        """Выполняет клик по вопросу и ожидает анимацию раскрытия ответа."""
        # Кликаем по вопросу
        self.click_to_element(question_element)

        # Ожидаем, пока ответ станет видимым
        locator = self.format_locator(MainPageLocators.ANSWER_TEMPLATE, index)
        self.wait_for_element_visible(locator, timeout=10)

    @allure.step('Получить текст ответа')
    def _get_answer_text(self, index: int) -> str:
        """Находит и возвращает текст ответа."""
        locator = self.format_locator(MainPageLocators.ANSWER_TEMPLATE, index)
        answer = self.wait_for_element_visible(locator, timeout=15)
        return answer.text

    @allure.step('Кликнуть на верхнюю кнопку "Заказать"')
    def click_header_order_button(self):
        """
        Кликает на кнопку 'Заказать' в шапке страницы.
        Предварительно прокручивает страницу к кнопке.
        """
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_HEADER)
        self.wait_for_element_clickable(MainPageLocators.ORDER_BUTTON_HEADER)
        self.click_to_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Кликнуть на центральную кнопку "Заказать"')
    def click_middle_order_button(self):
        """
        Кликает на большую центральную кнопку 'Заказать'.
        Предварительно прокручивает страницу к кнопке.
        """
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MIDDLE)
        self.wait_for_element_clickable(MainPageLocators.ORDER_BUTTON_MIDDLE)
        self.click_to_element(MainPageLocators.ORDER_BUTTON_MIDDLE)

    @allure.step('Проверить видимость верхней кнопки "Заказать"')
    def is_header_order_button_visible(self) -> bool:
        """Проверяет видимость кнопки заказа в шапке."""
        return self.is_element_present(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Проверить видимость центральной кнопки "Заказать"')
    def is_middle_order_button_visible(self) -> bool:
        """Проверяет видимость большой центральной кнопки заказа."""
        return self.is_element_present(MainPageLocators.ORDER_BUTTON_MIDDLE)

    @allure.step('Дождаться загрузки главной страницы')
    def wait_for_page_loaded(self):
        """Ожидает полной загрузки главной страницы."""
        self.wait_for_element_visible(MainPageLocators.ORDER_BUTTON_HEADER)