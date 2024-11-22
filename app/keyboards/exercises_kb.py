from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def inline_exercises():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Упражнения на грамматику", callback_data="grammar_exercises"))
    keyboard.add(InlineKeyboardButton(text="Упражнения на перевод предложений", callback_data="translate_exercises"))
    keyboard.add(InlineKeyboardButton(text=f"Назад⬛️", callback_data=f"back_to_modules"))
    return keyboard.adjust(1).as_markup()


async def back_to_exercises():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Назад⬛️", callback_data="exercises"))
    return keyboard.as_markup()


async def back_to_grammar_exercises():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Назад⬛️", callback_data="grammar_exercises"))
    return keyboard.as_markup()


async def back_to_translate_exercises():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Назад⬛️", callback_data="translate_exercises"))
    return keyboard.as_markup()