from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


back_to_input_words = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назад⬛️", callback_data="back_to_input_words no")]
])