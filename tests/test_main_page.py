import allure
import pytest
from data import AnswerText, QuestionText
from pages.main_page import MainPage


@allure.suite('Проверяем FAQ')
class TestMainPage:
    """Тесты для проверки раздела Часто задаваемых вопросов (FAQ)"""

    @allure.title("Проверка ответов на вопросы")
    @allure.description("Принимаем куки, скроллим страницу в самый низ, "
                        "кликаем поочерёдно на каждый вопрос и "
                        "сравниваем полученный ответ с ответом из словаря")
    @pytest.mark.parametrize("index", list(range(len(QuestionText.QUESTIONS))))
    def test_verify_faq_answer_correctness(self, driver, index):
        """
        Проверка корректности ответов в разделе FAQ

        Шаги:
        1. Принимаем соглашение об использовании cookies
        2. Получаем текст вопроса по указанному индексу
        3. Кликаем на вопрос и получаем фактический текст ответа
        4. Сравниваем фактический ответ с ожидаемым значением

        Аргументы:
            driver: фикстура для работы с браузером
            index: индекс вопроса в списке вопросов

        Проверки:
            - Фактический текст ответа соответствует ожидаемому
        """
        main_page = MainPage(driver)
        with allure.step('Принимаем куки'):
            main_page.accept_cookies()

        question_text = QuestionText.QUESTIONS[index]

        with allure.step(f'Кликаем на вопрос "{question_text}"'
                         f' и проверяем ответ'):
            expected_answer_text = AnswerText.ANSWERS[index]
            actual_answer_text = main_page.get_answer_text(index)
            assert actual_answer_text == expected_answer_text, (
                f'Ожидали ответ {expected_answer_text}, '
                f'получили {actual_answer_text}')