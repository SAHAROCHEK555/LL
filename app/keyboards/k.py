from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


# main keyboard
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📖обучение📖"), KeyboardButton(text="📌задачи📌")], 
    [KeyboardButton(text="📈ресурсы📈"), KeyboardButton(text="❓вопросы❓")],
    [KeyboardButton(text="📃помощь📃")]
], resize_keyboard=True)    

# kbs for tasks
tasks = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="выбрыть задачу", callback_data="choose_task")],
    [InlineKeyboardButton(text="активные задачи", callback_data="get_active_tasks")],
])

tasks_types = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="задача на день", callback_data="day_tasks")],
    [InlineKeyboardButton(text="задача на неделю", callback_data="week_tasks")],
    [InlineKeyboardButton(text="назад", callback_data="back to_task_planer")]
])

tasks_day = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="продать кому-то ручку", callback_data="choose_start day_one"), InlineKeyboardButton(text="изучить виды налогов", callback_data="choose_start day_two")],
    [InlineKeyboardButton(text="выучить основыне типы налогов для бизнеса", callback_data="choose_start day_three"), InlineKeyboardButton(text="посмотреть ставки кредитов для бизнеса", callback_data="choose_start day_four")],
    [InlineKeyboardButton(text="назад", callback_data="back to_types_of_tasks")]
])

tasks_week = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="повторить уроки бизнеса", callback_data="choose_start week_one"), InlineKeyboardButton(text="придумать идею для стартапа", callback_data="choose_start week_two")],
    [InlineKeyboardButton(text="разработать логотип", callback_data="choose_start week_three"), InlineKeyboardButton(text="сделать презентацию стартапа", callback_data="choose_start week_four")],
    [InlineKeyboardButton(text="назад", callback_data="back to_types_of_tasks")]
])

start_kbs = {"day_one": 
             InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="начать задачу", callback_data="start day_one")], [InlineKeyboardButton(text="назад", callback_data="back to_day_tasks")]]),
             "day_two": 
             InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="начать задачу", callback_data="start day_two")], [InlineKeyboardButton(text="назад", callback_data="back to_day_tasks")]]),
             "day_three": 
             InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="начать задачу", callback_data="start day_three")], [InlineKeyboardButton(text="назад", callback_data="back to_day_tasks")]]),
             "day_four": 
             InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="начать задачу", callback_data="start day_four")], [InlineKeyboardButton(text="назад", callback_data="back to_day_tasks")]]),
             "week_one": 
             InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="начать задачу", callback_data="start week_one")], [InlineKeyboardButton(text="назад", callback_data="back to_week_tasks")]]),
             "week_two": 
             InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="начать задачу", callback_data="start week_two")], [InlineKeyboardButton(text="назад", callback_data="back to_week_tasks")]]),
             "week_three": 
             InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="начать задачу", callback_data="start week_three")], [InlineKeyboardButton(text="назад", callback_data="back to_week_tasks")]]),
             "week_four": 
             InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="начать задачу", callback_data="start week_four")], [InlineKeyboardButton(text="назад", callback_data="back to_week_tasks")]]),
             }

empty_active_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="назад", callback_data="back to_task_planer")]])

async def get_finish_kb(key):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="завершить задачу", callback_data=f"finish {key}"))
    keyboard.add(InlineKeyboardButton(text="назад", callback_data="back to_active_tasks")) 
    return keyboard.adjust(1).as_markup()

async def get_kb_with_active_tasks(dct: dict):
    keyboard = InlineKeyboardBuilder()
    for name, val in dct.items():
        keyboard.add(InlineKeyboardButton(text=val, callback_data=f"choose_finish {name}"))
    keyboard.add(InlineKeyboardButton(text="назад", callback_data="back to_task_planer"))
    return keyboard.adjust(1).as_markup()

# kbs for learning
kb_for_lessons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="урок №1", callback_data="get_lesson 1"), InlineKeyboardButton(text="урок №2", callback_data="get_lesson 2")],
    [InlineKeyboardButton(text="урок №3", callback_data="get_lesson 3"), InlineKeyboardButton(text="урок №4", callback_data="get_lesson 4")]
])

back_to_lessons_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="назад", callback_data="back to_lessons")]])

# kbs for questions
questions_kb = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text="Можно ли вести бизнес без регистрации?", callback_data="get_question 1"), InlineKeyboardButton(text="Что регистрировать?", callback_data="get_question 2")],
    [InlineKeyboardButton(text="Какие документы нужны для регистрации ИП?", callback_data="get_question 3"), InlineKeyboardButton(text="Нужна ли предпринимателям лицензия?", callback_data="get_question 4")],
    [InlineKeyboardButton(text="Как получить лицензию?", callback_data="get_question 5"), InlineKeyboardButton(text="Почему название компании должно быть уникальным?", callback_data="get_question 6")],
    [InlineKeyboardButton(text="Зачем регистрируют авторские права?", callback_data="get_question 7"), InlineKeyboardButton(text="Как зарегистрировать бренд?", callback_data="get_question 8")],
    [InlineKeyboardButton(text="Есть ли правила использования логотипа?", callback_data="get_question 9"), InlineKeyboardButton(text="Что является плагиатом?", callback_data="get_question 10")],
])

back_to_questions_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="назад", callback_data="back to_questions")]])

#kbs for resources
resources_kb = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text="Приоритеты", callback_data="get_resources_advice 1"), InlineKeyboardButton(text="Потенциал", callback_data="get_resources_advice 2")],
    [InlineKeyboardButton(text="Координация?", callback_data="get_resources_advice 3"), InlineKeyboardButton(text="Использование технологий", callback_data="get_resources_advice 4")],
    [InlineKeyboardButton(text="Учет ресурсов", callback_data="get_resources_advice 5")]
])

back_to_resources_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="назад", callback_data="back to_resources")]])