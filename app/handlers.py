import asyncio
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from config import TEST_LEVEL_API_KEY, GRAMMAR_EXERCISES_API_KEY, EXPLATION_GRAMMAR_RULES_API_KEY, TRANSLATE_API_KEY, DAILY_WORDS_API_KEY, GENERATE_FLASHCARD_API_KEY
from database_api.WorkWithDatabase import WorkWithDataBase
from ai_api.MistralWork import MistralWork
import keyboards.languages_select_kb as languages_select_kb
import keyboards.level_language_select as level_language_select_kb
import keyboards.modules_select_kb as modules_select_kb
import keyboards.translate_keyboard as translate_kb
import keyboards.grammar_exercises_kb as grammar_exercises_kb
import keyboards.flashcard_kb as flashcardKb
import keyboards.everyday_words_phrases_kb as everyday_words_phrases_kb
import keyboards.exercises_kb as exercises_kb

router = Router()
user_message = F.data.split()
path = "database_api/database.json"
grammar_questions = ''
translate_questions = ''

#класс с состояниями FSM
class ModulesStates(StatesGroup):
    test_level_state = State()
    translate_state = State()
    grammar_explain_state = State()
    grammar_exercise_state = State()
    translate_exercise_state = State()
    

async def send_notifications(bot):
    while True:
        print("__#")
        english_collection = MistralWork.answer_from_mistral(DAILY_WORDS_API_KEY, "Пожелай мне удачи и поддержи меня в изуыении языка и дай мне подборку новых слов, с примерами их использования на этом языке: Английский. Без вступительного слова - конечно. Отвечай на русском.")
        franch_collection = MistralWork.answer_from_mistral(DAILY_WORDS_API_KEY, "Пожелай мне удачи и поддержи меня в изуыении языка и дай мне подборку новых слов с примерами их использования на этом языке: Фрацузский. Без вступительного слова - конечно. Отвечай на русском.")
        italian_collection = MistralWork.answer_from_mistral(DAILY_WORDS_API_KEY, "Пожелай мне удачи и поддержи меня в изуыении языка и дай мне подборку новых слов с примерами их использования на этом языке: Итальянский. Без вступительного слова - конечно. Отвечай на русском.")
        japanese_collection = MistralWork.answer_from_mistral(DAILY_WORDS_API_KEY, "Пожелай мне удачи и поддержи меня в изуыении языка и дай мне подборку новых слов с примерами их использования на этом языке: Японский. Без вступительного слова - конечно. Отвечай на русском.")
        spanish_collection = MistralWork.answer_from_mistral(DAILY_WORDS_API_KEY, "Пожелай мне удачи и поддержи меня в изуыении языка и дай мне подборку новых слов с примерами их использования на этом языке: Испанский. Без вступительного слова - конечно. Отвечай на русском.")
        german_collection = MistralWork.answer_from_mistral(DAILY_WORDS_API_KEY, "Пожелай мне удачи и поддержи меня в изуыении языка и дай мне подборку новых слов с примерами их использования на этом языке: Немецкий. Без вступительного слова - конечно. Отвечай на русском.")
        slovak_collection = MistralWork.answer_from_mistral(DAILY_WORDS_API_KEY, "Пожелай мне удачи и поддержи меня в изуыении языка и дай мне подборку новых слов с примерами их использования на этом языке: Словацкий. Без вступительного слова - конечно. Отвечай на русском.") 
        portugues_collection =MistralWork.answer_from_mistral(DAILY_WORDS_API_KEY, "Пожелай мне удачи и поддержи меня в изуыении языка и дай мне подборку новых слов с примерами их использования на этом языке: Португальский. Без вступительного слова - конечно. Отвечай на русском.")
        print("__2")
        new_words_collections = {
            "Английский": english_collection,
            "Фрацузский": franch_collection,
            "Итальянский": italian_collection,
            "Японский": japanese_collection,
            "Испанский": spanish_collection,
            "Португальский": portugues_collection,
            "Немецкий": german_collection,
            "Словацкий": slovak_collection
        }
        print("__3")
        users = WorkWithDataBase.get_all_users_list(path)
        for i in range(len(users)):
            language = WorkWithDataBase.read_data_from_database(users[i], "language", path)
            await bot.send_message(int(users[i]), new_words_collections[language])
            await asyncio.sleep(2*2)


#обработка команд start/restart
@router.message(Command("start", "restart"))
async def command_start(message: Message):
    WorkWithDataBase.make_database_user(message.from_user.id, path)    
    await message.answer("Выберите язык:", reply_markup=await languages_select_kb.languages_inline())


#возврат из выбора уровня в выбор языков
@router.callback_query(user_message[0] == "languages_select_back")
async def write_to_database(callback_query: CallbackQuery):
    await callback_query.message.edit_text("Выберите язык:", reply_markup=await languages_select_kb.languages_inline())


#обработка выбора языка
@router.callback_query(user_message[0] == "language")
async def write_to_database(callback_query: CallbackQuery):
    WorkWithDataBase.make_database_user(callback_query.from_user.id, path)
    WorkWithDataBase.write_data_to_database(callback_query.from_user.id, "language", callback_query.data.split()[1], path)
    await callback_query.message.edit_text("Выберите уровень владения языком:", reply_markup=await level_language_select_kb.levels_inline())


# возврат из автоматического определения уровня языка в ручной выбор уровня языка
@router.callback_query(user_message[0] == "types_of_tasks_back")
async def write_to_database(callback_query: CallbackQuery):
    await callback_query.message.edit_text("Выберите уровень владения языком:", reply_markup=await level_language_select_kb.levels_inline())


# получение уровня владения языком и открытие клавиатуры с основными модулями
@router.callback_query(user_message[0] == "level")
async def write_to_database(callback_query: CallbackQuery):
    WorkWithDataBase.write_data_to_database(callback_query.from_user.id, "level", callback_query.data.split()[1], path)
    language = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "language", path)
    await callback_query.message.edit_text(f"Язык: {language} \nУровень: {callback_query.data.split()[1]}", reply_markup=modules_select_kb.modules_inline)
    

# FSM для определение уровня языка
@router.callback_query(user_message[0] == "test_level")
async def give_test_for_user(callback_query: CallbackQuery, state: FSMContext):
    language = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "language", path)
    get_test_message = f"Привет! , дай мне тест на определение моего уровня в {language} (Начинающий, Средний, Продвинутый). Скинь только вопросы, я пришлю тебе ответы и ты вернёшь мне следующим сообщением из одного слова мой уровень"
    test_for_user = MistralWork.answer_from_mistral(TEST_LEVEL_API_KEY, get_test_message)
    await state.set_state(ModulesStates.test_level_state)
    await callback_query.message.edit_text(test_for_user, reply_markup=level_language_select_kb.back_to_level_select)


# продолжение
@router.message(ModulesStates.test_level_state)
async def get_level(user_message: Message):
    user_level = MistralWork.answer_from_mistral(TEST_LEVEL_API_KEY, f"Мои ответы - {user_message.text}. Отправь мне мой уровень одиним словом без знаков препинания (Начинающий, Средний, Продвинутый).")
    WorkWithDataBase.write_data_to_database(user_message.from_user.id, "level", user_level, path)
    language = WorkWithDataBase.read_data_from_database(user_message.from_user.id, "language", path)
    await user_message.answer(f"Язык: {language}\nУровень: {user_level}", reply_markup=modules_select_kb.modules_inline)


# переводчик
@router.callback_query(user_message[0] == "translate")
async def translate_info_for_user(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(ModulesStates.translate_state)
    await callback_query.message.edit_text("Напишите слово/предложение для перевода: ", reply_markup=modules_select_kb.back_to_modules)


@router.message(ModulesStates.translate_state)
async def get_translated_text(user_message: Message):
    translated_text = MistralWork.answer_from_mistral(TRANSLATE_API_KEY, f"Переведи это слово/предложение на русский язык {user_message.text}.")
    await user_message.answer(translated_text, reply_markup=translate_kb.back_to_input_words)


#возврат к модулям из ввода слов
@router.callback_query(user_message[0] == "back_to_modules")
async def back_to_modules(callback_query: CallbackQuery):
    language = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "language", path)
    level = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "level", path)
    await callback_query.message.edit_text(f"Язык: {language} \nУровень: {level}", reply_markup=modules_select_kb.modules_inline)


#вернуться из модулей в выбор уровня
@router.callback_query(user_message[0] == "back_to_level_select")
async def back_to_level_select(callback_query: CallbackQuery):
    await callback_query.message.edit_text("Выберите уровень владения языком:", reply_markup=await level_language_select_kb.levels_inline())


@router.callback_query(user_message[0] == "exercises")
async def exercises(callback_query: CallbackQuery):
    await callback_query.message.edit_text("Выбери упражнение", reply_markup=await exercises_kb.inline_exercises())


@router.callback_query(user_message[0] == "grammar_exercises")
async def grammar_exercises(callback_query: CallbackQuery, state: FSMContext):
    global grammar_questions
    await state.set_state(ModulesStates.grammar_exercise_state)
    language = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "language", path)
    level = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "level", path)
    get_tasks_message = f"Привет! Пожалуйста, дай мне задание на знание грамматики языка {language} для ученика, знающего язык на уровне {level}. Скинь только один вопрос, я пришлю тебе ответ и ты вернёшь мне следующим сообщением верно ли решено задание"
    questions_for_user = MistralWork.answer_from_mistral(GRAMMAR_EXERCISES_API_KEY, get_tasks_message)
    grammar_questions = questions_for_user
    await callback_query.message.edit_text(questions_for_user, reply_markup=await exercises_kb.back_to_exercises())


@router.message(ModulesStates.grammar_exercise_state)
async def get_grammar_answer(user_message: Message):
    grammar_answer = MistralWork.answer_from_mistral(GRAMMAR_EXERCISES_API_KEY, f"{grammar_questions} - это вопросы. {user_message.text}. Это ответы на вопросы. Проверь правильность ответов, и, если есть ошибки, поясни их. Только разбор, без лишней информации")
    await user_message.answer(grammar_answer, reply_markup=await exercises_kb.back_to_exercises())


@router.callback_query(user_message[0] == "translate_exercises")
async def translate_exercises(callback_query: CallbackQuery, state: FSMContext):
    global translate_questions
    await state.set_state(ModulesStates.translate_exercise_state)
    language = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "language", path)
    level = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "level", path)
    get_tasks_message = f"Привет! Пожалуйста, дай мне задание на перевод небольшого текста на языке {language} для ученика, знающего язык на уровне {level}. Скинь только текст, я пришлю тебе перевод и ты вернёшь мне следующим сообщением верно ли решено задание"
    questions_for_user = MistralWork.answer_from_mistral(GRAMMAR_EXERCISES_API_KEY, get_tasks_message)
    translate_questions = questions_for_user
    await callback_query.message.edit_text(questions_for_user, reply_markup=await exercises_kb.back_to_exercises())


@router.message(ModulesStates.translate_exercise_state)
async def get_translate_answer(user_message: Message):
    translate_answer = MistralWork.answer_from_mistral(GRAMMAR_EXERCISES_API_KEY, f"{translate_questions} - это вопросы. {user_message.text}. Это ответы на вопросы. Проверь правильность ответов, и, если есть ошибки, поясни их. Только разбор, без лишней информации")
    await user_message.answer(translate_answer, reply_markup=await exercises_kb.back_to_exercises())


@router.callback_query(user_message[0] == "explation")
async def set_grammar_explain_responce(callback_query: CallbackQuery, state: FSMContext): 
    await state.set_state(ModulesStates.grammar_explain_state)
    await callback_query.message.edit_text("Напишите грамматическое правило для объяснения: ", reply_markup=modules_select_kb.back_to_modules)


@router.message(ModulesStates.grammar_explain_state)
async def grammar_handler(message: Message, state: FSMContext):
    await state.update_data(responce = message.text)
    data = await state.update_data()

    language = WorkWithDataBase.read_data_from_database(message.from_user.id, "language", path)
    level = WorkWithDataBase.read_data_from_database(message.from_user.id, "level", path)

    message_answer = MistralWork.answer_from_mistral(EXPLATION_GRAMMAR_RULES_API_KEY, f"представь что ты учитель иностранного языка и обьяснишяешь мне {data['responce']} в {language} для ученика {level} уровня")
    await message.answer(text = message_answer)
    await state.clear()

@router.callback_query(user_message[0] == "flashcards")
async def flashcard_handler_first(callback_query: CallbackQuery): 
    await callback_query.message.edit_text("Выберите действие", reply_markup=flashcardKb.generate_flashcard)

@router.callback_query(user_message[0] == "generate_flashcard")
async def flashcard_handler_twice(callback_query: CallbackQuery):
    await callback_query.message.edit_text('Генерируем запрос...')
    language = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "language", path)
    level = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "level", path)
    text = MistralWork.answer_from_mistral(GENERATE_FLASHCARD_API_KEY, f"Сгенерируй новое слово или новую фразу на {language} языке затем поставь 123 и после него запиши перевод на русский язык.")

    global translate
    txt = text.split('123')[0]
    translate = text.split('123')[1]
    await callback_query.message.edit_text(txt, reply_markup=flashcardKb.show_flashcard_translate)

@router.callback_query(user_message[0] == "show_translate")
async def flashcard_handler_twice(callback_query: CallbackQuery):
    await callback_query.message.edit_text(translate, reply_markup=modules_select_kb.back_to_modules)  
