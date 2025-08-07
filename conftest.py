import allure
import pytest
from selenium import webdriver
from data import URLs
from helpers import generate_random_order_data


# Фикстура драйвера для Mozilla Firefox
@pytest.fixture()
@allure.title("Подготовка драйвера Firefox")
def driver():
    """
    Фикстура для инициализации и настройки веб-драйвера Firefox.

    Основные функции:
    1. Создает экземпляр Firefox с заданными параметрами
    2. Устанавливает фиксированный размер окна 1920x1080
    3. Открывает главную страницу приложения
    4. Передает управление драйвером тестовой функции
    5. Корректно закрывает браузер после выполнения теста

    Конфигурация:
    - Используется стандартный профиль Firefox
    - Размер окна фиксируется для стабильности тестов
    - URL берется из конфигурационного файла URLs

    Returns:
        WebDriver: Экземпляр веб-драйвера Firefox готовый к использованию в тестах
    """
    # Создаем объект для настройки опций Firefox
    firefox_options = webdriver.FirefoxOptions()

    # Устанавливаем размер окна браузера
    firefox_options.add_argument('--width=1920')
    firefox_options.add_argument('--height=1080')

    # Инициализируем драйвер Firefox с заданными опциями
    driver = webdriver.Firefox(options=firefox_options)

    # Открываем главную страницу приложения
    driver.get(URLs.main_page)

    # Передаем драйвер в тестовую функцию
    yield driver

    # Закрываем браузер после завершения всех тестов
    driver.quit()


@pytest.fixture
def random_order_data():
    """Фикстура для генерации случайных данных заказа"""
    return generate_random_order_data()