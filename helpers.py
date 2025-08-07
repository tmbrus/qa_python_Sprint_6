import random
from datetime import datetime, timedelta


def generate_random_order_data():
    """
    Генерирует случайные данные для заполнения формы заказа самоката.

    Возвращает словарь со следующими ключами:
        - name: случайное имя
        - surname: случайная фамилия
        - address: случайный адрес
        - metro: случайная станция метро из списка
        - phone: случайный 11-значный номер телефона
        - date: случайная дата в 2025 году начиная с 03.08 в формате DD.MM.YYYY
        - duration: случайный срок аренды
        - color: случайный цвет самоката
        - comment: случайный комментарий (может быть пустым)

    Пример возвращаемого значения:
    {
        'name': 'Дмитрий',
        'surname': 'Курохтин',
        'address': 'Москва, ул. Плеханова',
        'metro': 'Перово',
        'phone': 79004962808,
        'date': '15.08.2025',
        'duration': 'сутки',
        'color': 'black',
        'comment': 'Подъезд со двора'
    }
    """
    # Константы для генерации данных
    METRO_STATIONS = [
        "Перово",
        "Чистые пруды",
        "Лубянка",
        "Охотный ряд",
        "Библиотека им. Ленина",
        "Парк культуры",
        "Краснопресненская",
        "Курская",
        "ВДНХ",
        "Третьяковская"
    ]
    COLORS = ['black', 'grey']
    RENTAL_DURATIONS = [
        'сутки', 'двое суток', 'трое суток', 'четверо суток',
        'пятеро суток', 'шестеро суток', 'семеро суток'
    ]

    # Генерация даты в 2025 году (от 03.08 до 31.12)
    start_date = datetime(2025, 8, 3).date()
    end_date = datetime(2025, 12, 31).date()
    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)
    order_date = (start_date + timedelta(days=random_days)).strftime('%d.%m.%Y')

    return {
        'name': random.choice(['Александр', 'Алексей', 'Дмитрий', 'Михаил', 'Иван']),
        'surname': random.choice(['Иванов', 'Петров', 'Смирнов', 'Соколов', 'Курохтин']),
        'address': random.choice(['Москва, ул. Пушкина', 'Тамбов 68',
                                  'Питер, Ул. Арбат', 'Химки, ул. Московская']),
        'metro': random.choice(METRO_STATIONS),
        'phone': random.randint(79000000000, 79999999999),  # Российский номер
        'date': order_date,  # Используем сгенерированную дату
        'duration': random.choice(RENTAL_DURATIONS),
        'color': random.choice(COLORS),
        'comment': random.choice(['', 'Позвонить за 15 минут до доставки',
                                  'Нет домофона, жду у подъезда', 'Подъезд со двора'])
    }