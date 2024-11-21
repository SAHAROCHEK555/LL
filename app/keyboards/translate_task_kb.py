from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def inline_text_ask():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Задание на перевод", callback_data="text_task"))
    return keyboard.adjust(2).as_markup()