import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Получаем текст ответа для вопроса {index}')
    def get_answer_text(self, index):
        """
        Получает текст ответа на вопрос FAQ по указанному индексу

        Args:
            index (int): Номер вопроса в списке FAQ (начиная с 0)

        Returns:
            str: Текст ответа на выбранный вопрос

        Steps:
            1. Формирует локаторы для вопроса и ответа по шаблону
            2. Скроллит страницу до вопроса для гарантированной видимости элемента
            3. Кликает по вопросу, чтобы раскрыть ответ
            4. Получает и возвращает текст ответа

        Example:
            get_faq_answer_by_index(0) → возвращает текст ответа для первого вопроса
        """
        # Формируем локатор для вопроса по шаблону с переданным индексом
        question_locator = self.format_locators(
            MainPageLocators.QUESTION_TEMPLATE, index)

        # Формируем локатор для ответа по шаблону с переданным индексом
        answer_locator = self.format_locators(
            MainPageLocators.ANSWER_TEMPLATE, index)

        # Скроллим страницу до элемента вопроса (передаем локатор)
        self.scroll_to_element(question_locator)

        # Кликаем по вопросу, чтобы раскрыть ответ
        self.click_to_element(question_locator)

        # Получаем текст из элемента ответа
        answer_text = self.get_element_text(answer_locator)

        return answer_text