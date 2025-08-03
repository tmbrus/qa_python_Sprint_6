import allure

from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    """Класс для работы со страницей оформления заказа"""

    @allure.step('Создание заказа по кнопке в верхней части страницы')
    def create_order_from_header(self, order_dict):
        """
        Оформление заказа через верхнюю кнопку 'Заказать'

        Args:
            order_dict: Словарь с данными для заполнения формы заказа

        Steps:
            1. Принять куки
            2. Проскроллить к верхней кнопке заказа
            3. Нажать кнопку заказа
            4. Заполнить первую страницу формы
            5. Перейти на вторую страницу формы
            6. Заполнить вторую страницу формы
            7. Подтвердить заказ
        """
        self.accept_cookies()
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_HEADER)
        self.click_to_element(MainPageLocators.ORDER_BUTTON_HEADER)
        self.fill_first_form(order_dict)
        self.go_to_next_form()
        self.fill_second_form(order_dict)
        self.confirm_order()

    @allure.step('Создание заказа по кнопке в нижней части страницы')
    def create_order_from_bottom(self, order_dict):
        """
        Оформление заказа через нижнюю кнопку 'Заказать'

        Args:
            order_dict: Словарь с данными для заполнения формы заказа

        Steps:
            1. Принять куки
            2. Проскроллить страницу вниз
            3. Найти и нажать нижнюю кнопку заказа
            4. Заполнить первую страницу формы
            5. Перейти на вторую страницу формы
            6. Заполнить вторую страницу формы
            7. Подтвердить заказ
        """
        self.accept_cookies()
        self.scroll_to_bottom()
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON_ALL_SIZES)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_ALL_SIZES)
        self.fill_first_form(order_dict)
        self.go_to_next_form()
        self.fill_second_form(order_dict)
        self.confirm_order()

    @allure.step('Переход к следующей форме')
    def go_to_next_form(self):
        """Переход от первой ко второй странице формы заказа"""
        self.scroll_to_element(OrderPageLocators.NEXT_BUTTON)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Подтверждение заказа')
    def confirm_order(self):
        """
        Подтверждение оформленного заказа

        Steps:
            1. Нажать кнопку 'Заказать'
            2. Подтвердить заказ в модальном окне
        """
        self.scroll_to_element(OrderPageLocators.MAKE_ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.MAKE_ORDER_BUTTON)
        self.scroll_to_element(OrderPageLocators.YES_BUTTON)
        self.click_to_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Заполняем первую форму заказа "Для кого самокат"')
    def fill_first_form(self, order_dict):
        """
        Заполнение персональных данных заказчика

        Args:
            order_dict: Словарь с данными клиента (имя, фамилия, адрес и т.д.)
        """
        self.fill_field(OrderPageLocators.NAME_INPUT, order_dict.get('name'))
        self.fill_field(OrderPageLocators.SURNAME_INPUT, order_dict.get('surname'))
        self.fill_field(OrderPageLocators.ADDRESS_INPUT, order_dict.get('address'))
        self.click_to_element(OrderPageLocators.METRO_INPUT)
        station_locator = OrderPageLocators.METRO_STATION_VISIBLE
        self.select_metro_station(station_locator, order_dict['metro'])
        self.fill_field(OrderPageLocators.PHONE_INPUT, order_dict.get('phone'))

    @allure.step('Заполняем вторую форму заказа "Про аренду"')
    def fill_second_form(self, order_dict):
        """
        Заполнение данных об аренде

        Args:
            order_dict: Словарь с данными аренды (дата, срок, цвет и т.д.)
        """
        self.set_rental_date(order_dict.get('date'))
        self.select_rental_period(order_dict.get('duration'))
        color_locator = (OrderPageLocators.COLOR_BLACK_CHECKBOX
                         if order_dict.get('color') == 'black' else
                         OrderPageLocators.COLOR_GREY_CHECKBOX)
        self.click_to_element(color_locator)
        self.fill_field(OrderPageLocators.COMMENT_INPUT, order_dict.get('comment'))

    @allure.step('Установить дату проката')
    def set_rental_date(self, date_string):
        """Установка даты начала аренды"""
        date_field = self.wait_for_element_visible(OrderPageLocators.DATE_INPUT)
        date_field.clear()
        date_field.send_keys(date_string)
        # Клик в любое место, чтобы закрыть календарь
        self.click_by_tag_name('body')

    @allure.step('Выбор срока аренды')
    def select_rental_period(self, duration):
        """Выбор продолжительности аренды из выпадающего списка"""
        self.scroll_to_element(OrderPageLocators.RENTAL_DURATION_DROPDOWN)
        self.click_to_element(OrderPageLocators.RENTAL_DURATION_DROPDOWN)
        duration_option_locator = (
            By.XPATH,
            OrderPageLocators.RENTAL_DURATION_OPTION[1].format(duration)
        )
        self.scroll_to_element(duration_option_locator)
        self.click_to_element(duration_option_locator)

    @allure.step('Проверяем наличие окна с информацией о заказе')
    def check_order_status_window(self):
        """Проверка отображения окна подтверждения заказа"""
        return self.wait_for_element_visible(OrderPageLocators.STATUS_WINDOW)

    @allure.step('Выбираем станцию метро')
    def select_metro_station(self, locator, station_name):
        """
        Выбор станции метро из выпадающего списка

        Args:
            locator: Локатор списка станций
            station_name: Название станции для выбора
        """
        self.wait_for_element_visible(locator)
        stations = self.find_elements_with_wait(locator)
        for station in stations:
            if station.text.strip() == station_name:
                station.click()
                break
