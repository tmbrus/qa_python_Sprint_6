from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Класс для хранения локаторов элементов главной страницы.
    Содержит локаторы для раздела FAQ и кнопок заказа.
    """

    # Шаблон локатора для вопроса FAQ по индексу {0}
    # Пример: //div[@id='accordion__heading-0'] - первый вопрос
    QUESTION_TEMPLATE = (By.XPATH, "//div[@id='accordion__heading-{0}']")

    # Шаблон локатора для ответа FAQ по индексу {0}
    # Пример: //div[@id='accordion__panel-0'] - ответ на первый вопрос
    ANSWER_TEMPLATE = (By.XPATH, "//div[@id='accordion__panel-{0}']")

    # Кнопка "Заказать" в верхней части страницы (в шапке)
    # Находится по:
    # - классу Button_Button
    # - тексту "Заказать"
    ORDER_BUTTON_HEADER = (By.XPATH, '//button[contains('
                                     '@class, "Button_Button") and contains('
                                     'text(), "Заказать")]')

    # Кнопка "Заказать" в середине страницы
    # (большая центральная кнопка)
    # Находится по:
    # - классу Button_Button
    # - классу Button_Middle (уникальный для этой кнопки)
    # - тексту "Заказать"
    ORDER_BUTTON_MIDDLE = (By.XPATH, '//button[contains(@class,'
                                     ' "Button_Button") and contains('
                                     '@class, "Button_Middle") and contains('
                                     'text(), "Заказать")]')

    # Локатор кнопки принятия cookies
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')











