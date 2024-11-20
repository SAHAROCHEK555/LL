from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def inline_words_phrases():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Ежедневное слово или фраза", callback_data="everyday_words_phrases"))
    return keyboard.adjust(2).as_markup()
