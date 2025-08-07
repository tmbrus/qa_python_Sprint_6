from selenium.webdriver.common.by import By


class OrderPageLocators:
    """
    Класс для хранения локаторов элементов страницы оформления заказа.
    Содержит локаторы для всех полей форм и кнопок.
    """

    # ===== Форма "Для кого самокат" =====
    # Поле ввода имени
    NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    # Поле ввода фамилии
    SURNAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    # Поле ввода адреса доставки
    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")

    # Поле выбора станции метро
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    # Шаблон локатора для конкретной станции метро (подставляется значение)
    METRO_STATION_TEMPLATE = '//button[@data-value="{value}"]'
    # Все доступные станции метро в выпадающем списке
    METRO_STATION_ALL = (By.XPATH, '//*[@class="select-search__option"]')
    # Видимые станции метро в выпадающем списке
    METRO_STATION_VISIBLE = (By.XPATH, '//*[@class="select-search__row" '
                                       'and @role="menuitem"]')

    # Поле ввода номера телефона
    PHONE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    # Кнопка перехода к следующей форме ("Далее")
    NEXT_BUTTON = (By.XPATH, '//button[contains(text(), "Далее")]')

    # ===== Форма "Про аренду" =====
    # Поле ввода даты доставки
    DATE_INPUT = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
    # Локатор текущего дня в календаре
    DAY_LOCATOR = (By.XPATH, './/div[contains(@class, "react-datepicker__day--today")]')

    # Выпадающий список для выбора срока аренды
    RENTAL_DURATION_DROPDOWN = (By.XPATH, '//div[@class="Dropdown-control"]')
    # Шаблон локатора для конкретного срока аренды (подставляется значение)
    RENTAL_DURATION_OPTION = (By.XPATH, '//div[@class="Dropdown-menu"]//div[text()="{}"]')

    # Чекбоксы выбора цвета самоката
    COLOR_BLACK_CHECKBOX = (By.ID, "black")  # Черный цвет
    COLOR_GREY_CHECKBOX = (By.ID, "grey")  # Серый цвет

    # Поле для комментария курьеру
    COMMENT_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Комментарий')]")
    # Основная кнопка оформления заказа
    MAKE_ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Middle") '
                                   'and contains(text(), "Заказать")]')

    # Альтернативные кнопки "Заказать" (для разных размеров экрана)
    ORDER_BUTTON_ALL_SIZES = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]'
                                        '/button[contains(@class, "Button_Button") '
                                        'and contains(text(), "Заказать")]')

    # ===== Форма подтверждения заказа =====
    # Кнопка подтверждения заказа ("Да")
    YES_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button") '
                            'and contains(text(), "Да")]')

    # Окно с информацией о статусе заказа
    STATUS_WINDOW = (By.XPATH, '//div[contains(@class,"Order_ModalHeader")]')