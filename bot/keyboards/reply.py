from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def start() -> ReplyKeyboardMarkup:
    """
    Reply-клавиатура с кнопками "Вакансии" и "Загрузить резюме".

    :return: ReplyKeyboardMarkup
    """

    button = [
        [KeyboardButton(text="💼 Вакансии")],
        [KeyboardButton(text="📄 Загрузить резюме")],
    ]
    return ReplyKeyboardMarkup(
        keyboard=button,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Выбери раздел",
    )