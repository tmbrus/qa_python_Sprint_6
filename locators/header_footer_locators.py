from selenium.webdriver.common.by import By


class HeaderFooterLocators:
    """
    Класс локаторов для элементов шапки и подвала сайта.
    Содержит локаторы кнопок, логотипов и других элементов,
    расположенных в верхней или нижней части страницы.
    """

    # Кнопка подтверждения использования cookies
    # Находится по:
    # - ID "rcc-confirm-button"
    # - классу "App_CookieButton"
    COOKIE_BUTTON = (By.XPATH, '//button[@id="rcc-confirm-button" and '
                             'contains(@class, "App_CookieButton")]')

    # Логотип Яндекс в шапке сайта
    # Находится по классу "Header_LogoYandex"
    YANDEX_LOGO = (
        By.XPATH,
        "//*[contains(@class, 'Header_LogoYandex')]")

    # Логотип "Самокат" в шапке сайта
    # Находится по классу "Header_LogoScooter"
    SAMOKAT_LOGO = (
        By.XPATH,
        "//*[contains(@class, 'Header_LogoScooter')]")

    # Логотип Дзен (отображается после перехода по логотипу Яндекса)
    # Находится по атрибуту aria-label="Логотип Бренда"
    DZEN_LOGO = (By.XPATH, '//a[@aria-label="Логотип Бренда"]')