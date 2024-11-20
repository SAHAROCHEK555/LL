from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


levels = ["Начианющий", "Средний", "Продвинутый"]

async def inline_levels():
    keyboard = InlineKeyboardBuilder()
    for level in levels:
        keyboard.add(InlineKeyboardButton(text=f"{level}", callback_data=f"level {level}"))
    keyboard.add(InlineKeyboardButton(text=f"Определить", callback_data=f"test_level no"))
    keyboard.add(InlineKeyboardButton(text=f"Назад⬛️", callback_data=f"languages_select_back no"))
    return keyboard.adjust(2).as_markup()

level_select_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назад⬛️", callback_data="types_of_tasks_back no")]
])