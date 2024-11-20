from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def inline_exercises():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Упражнения на знание языка", callback_data="grammar_exercises"))
    # keyboard.add(InlineKeyboardButton(text=f"Назад⬛️", callback_data=f"languages_select_back no"))
    # выше будет возврат на основную клавиатуру, когда пользователю надоест решать упражнения
    return keyboard.adjust(2).as_markup()

async def exercises_continue():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Назад⬛️", callback_data="back_to_types_of_tasks"))
    keyboard.add(InlineKeyboardMarkup(text="Новое задание", callback_data="grammar_exercises"))