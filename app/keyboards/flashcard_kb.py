from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

generate_flashcard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Сгенерировать карточку", callback_data="generate_flashcard")],
    [InlineKeyboardButton(text="Назад⬛️", callback_data="back_to_modules")]
])

show_flashcard_translate = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="показать перевод", callback_data="show_translate")],
    [InlineKeyboardButton(text="Назад⬛️", callback_data="flashcards")]
])

back_to_flashcards = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Назад⬛️", callback_data="flashcards")]
])