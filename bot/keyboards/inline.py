from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def vacancies(position_index: int, set_number: int) -> InlineKeyboardMarkup:
    """
    Inline-клавиатура для навигации между вакансиями.

    :param position_index: номер вакансии
    :param set_number: номер набора вакансий
    """

    builder = InlineKeyboardBuilder()

    if position_index == 0:
        builder.row(
            InlineKeyboardButton(text="➡️ Вперёд", callback_data=f"vacancy:1:{set_number}")
        )
    elif position_index == 1:
        builder.row(
            InlineKeyboardButton(text="⬅️ Назад", callback_data=f"vacancy:0:{set_number}"),
            InlineKeyboardButton(text="➡️ Вперёд", callback_data=f"vacancy:2:{set_number}")
        )
    elif position_index == 2:
        builder.row(
            InlineKeyboardButton(text="⬅️ Назад", callback_data=f"vacancy:1:{set_number}")
        )

    return builder.as_markup()

def key_skills() -> InlineKeyboardMarkup:
    """
    Inline-клавиатура для подтверждения извлечения ключевых навыков из резюме.

    """

    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Да", callback_data="yes"),
        InlineKeyboardButton(text="Нет", callback_data="no")
    )
    return builder.as_markup()