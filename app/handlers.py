from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from config import TEST_LEVEL_API_KEY, GRAMMAR_EXERCISES_API_KEY, EXPLATION_GRAMMAR_RULES_API_KEY, TRANSLATE_API_KEY
from database_api.WorkWithDatabase import WorkWithDataBase
from ai_api.MistralWork import MistralWork
import keyboards.languages_select_kb as languages_select_kb
import keyboards.level_language_select as level_language_select_kb
import keyboards.modules_select_kb as modules_select_kb
import keyboards.translate_keyboard as translate_kb
import keyboards.everyday_words_phrases_kb as everyday_words_phrases_kb
import keyboards.grammar_exercises_kb as grammar_exercises_kb

router = Router()
user_message = F.data.split()
path = "database_api/database.json"


#класс с состояиниями FSM
class ModulesStates(StatesGroup):
    test_level_state = State()
    translate_state = State()

class Reg_grammar(StatesGroup):
    responce = State()

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



#возврат из автоматического определения уровня языка в ручной выбор уровня языка
@router.callback_query(user_message[0] == "types_of_tasks_back")
async def write_to_database(callback_query: CallbackQuery):
    await callback_query.message.edit_text("Выберите уровень владения языком:", reply_markup=await level_language_select_kb.levels_inline())



#получение уровня владения языком и открытие клавиатуры с основными модулями
@router.callback_query(user_message[0] == "level")
async def write_to_database(callback_query: CallbackQuery):
    WorkWithDataBase.write_data_to_database(callback_query.from_user.id, "level", callback_query.data.split()[1], path)
    language = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "language", path)
    await callback_query.message.edit_text(f"Язык: {language} \nУровень: {callback_query.data.split()[1]}", reply_markup=modules_select_kb.modules_inline)
    

#FSM для определение уровня языка
@router.callback_query(user_message[0] == "test_level")
async def give_test_for_user(callback_query: CallbackQuery, state: FSMContext):
    language = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "language", path)
    get_test_message = f"Привет! Пожалуйста, дай мне тест на определение моего уровня в {language} (Начинающий, Средний, Продвинутый). Скинь только вопросы, я пришлю тебе ответы и ты вернёшь мне следующим сообщением из одного слова мой уровень"
    test_for_user = MistralWork.answer_from_mistral(TEST_LEVEL_API_KEY, get_test_message)
    await state.set_state(ModulesStates.test_level_state)
    await callback_query.message.edit_text(test_for_user, reply_markup=level_language_select_kb.back_to_level_select)
     
# продолжение
@router.message(ModulesStates.test_level_state)
async def get_level(user_message: Message, state: FSMContext):
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


#возврат из полученного перевода в ввод иностранного слова
@router.callback_query(user_message[0] == "back_to_input_words")
async def translate_info_for_user(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(ModulesStates.translate_state)
    await callback_query.message.edit_text("Напишите слово/предложение для перевода: ", reply_markup=modules_select_kb.back_to_modules)


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

@router.callback_query(user_message[0] == "grammar_exercises")
async def grammar_exercises(callback_query: CallbackQuery):
    language = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "language", path)
    level = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "level", path)
    get_tasks_message = f"Привет! Пожалуйста, дай мне задание на знание языка {language} для ученика, знающего язык на уровне {level}. Скинь только вопросы, я пришлю тебе ответы и ты вернёшь мне следующим сообщением верно ли решены задания"
    tasks_for_user = MistralWork.answer_from_mistral(EXPLATION_GRAMMAR_RULES_API_KEY, get_tasks_message)
    await callback_query.message.edit_text(tasks_for_user, reply_markup=await grammar_exercises_kb.inline_exercises())


@router.callback_query(user_message[0] == "everyday_words_exercises")
async def everyday_words_phrases(callback_query: CallbackQuery):
    language = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "language", path)
    level = WorkWithDataBase.read_data_from_database(callback_query.from_user.id, "level", path)
    get_words_message = f"Привет! Пожалуйста, дай мне слово или фразу на языке {language} для ученика, знающего язык на уровне {level}. Скинь только слово/фразу и перевод"
    tasks_for_user = MistralWork.answer_from_mistral(EXPLATION_GRAMMAR_RULES_API_KEY, get_words_message)
    await callback_query.message.edit_text(tasks_for_user, reply_markup=await everyday_words_phrases_kb.inline_words_phrases())

@router.callback_query(user_message[0] == "explation")
async def set_grammar_explain_responce(callback_query: CallbackQuery, state: FSMContext): 
    await state.set_state(Reg_grammar.responce)
    await callback_query.message.edit_text("Напишите какое грамматическое вам объяснить", reply_markup=modules_select_kb.back_to_modules)

@router.message(Reg_grammar.responce)
async def grammar_handler(message: Message, state: FSMContext):
    await state.update_data(responce = message.text)
    data = await state.update_data()

    language = WorkWithDataBase.read_data_from_database(message.from_user.id, "language", path)
    level = WorkWithDataBase.read_data_from_database(message.from_user.id, "level", path)

    message_answer = MistralWork.answer_from_mistral(EXPLATION_GRAMMAR_RULES_API_KEY, f"представь что ты учитель иностранного языка и обьяснишь мне {data['responce']} в {language} для ученика {level} уровня")
    await message.answer(text = message_answer)
    await state.clear()