from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


modules_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Переводчик", callback_data="translate")],
    [InlineKeyboardButton(text="Упражнения", callback_data="exercise")],
    [InlineKeyboardButton(text="Объяснения", callback_data="explation")],
    [InlineKeyboardButton(text="Назад⬛️", callback_data="back_to_level_select")]
])

back_to_modules = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назад⬛️", callback_data="back_to_modules")]
])
