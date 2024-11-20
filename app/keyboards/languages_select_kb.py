from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


languages_names = ["Английский", "Француский", "Японский", "Испанский", "Итальянский", "Немецкий", "Португальский", "Словацкий"]


async def inline_languages():
    keyboard = InlineKeyboardBuilder()
    for language in languages_names:
        keyboard.add(InlineKeyboardButton(text=f"{language} язык", callback_data=f"language {language}"))
    return keyboard.adjust(2).as_markup()
