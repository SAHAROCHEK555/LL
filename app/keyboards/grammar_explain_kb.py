from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def inline_explain_grammar():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Объяснение грамматических правил", callback_data="explain_grammar"))
    return keyboard.adjust(2).as_markup()