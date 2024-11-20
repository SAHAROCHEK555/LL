from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


levels = ["Начианющий", "Средний", "Продвинутый"]

async def levels_inline():
    keyboard = InlineKeyboardBuilder()
    for level in levels:
        keyboard.add(InlineKeyboardButton(text=f"{level}", callback_data=f"level {level}"))
    keyboard.add(InlineKeyboardButton(text=f"Определить", callback_data=f"test_level no"))
    keyboard.add(InlineKeyboardButton(text=f"Назад⬛️", callback_data=f"back_to_languages_select no"))
    return keyboard.adjust(2).as_markup()

back_to_level_select = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назад⬛️", callback_data="back_to_level_select no")]
])