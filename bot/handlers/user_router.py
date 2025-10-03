from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
import bot.keyboards.inline as ikb
import bot.keyboards.reply as rkb
from utils.utils import return_vacancies, extract_text_from_pdf, extract_text_from_docx
from utils.async_utils import async_http
from collections import defaultdict

router = Router()

# команда /start
@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("""Здравствуй👋🏻
Я постараюсь помочь тебе найти работу!

/resume - отправь мне резюме и я подскажу что можно улучшить.
/search - покажу тебе подходящие вакансии и вместе решим куда лучше откликнуться.
""", reply_markup=rkb.start())

class Resume(StatesGroup):
    sending_resume = State()

# команда /resume
@router.message(F.text == "📄 Загрузить резюме")
@router.message(Command("resume"))
async def resume_command(message: Message, state: FSMContext):
    # ожидание получения файла
    await state.set_state(Resume.sending_resume)

    await message.answer("""⬇️ Отправь мне своё резюме в формате PDF или DOCX и я выведу его текст.""")

# receiving a request from a user
@router.message(Resume.sending_resume)
async def sending_resume_state(message: Message, state: FSMContext):
    # проверка отправил ли пользователь файл
    if not message.document:
        await message.reply("Отправь мне текстовый файл твоего резюме в формате PDF или DOCX")
        return

    # проверка формата файла
    file_name = message.document.file_name.lower()
    if not (file_name.endswith(".pdf") or file_name.endswith(".docx")):
        await message.reply("Загрузи файл формата PDF или DOCX")
        return

    # подтверждение получения файла
    file_name = message.document.file_name
    await message.answer(f"Файл <b><i>{file_name.rsplit(".", 1)[0]}</i></b> получен!")
    file = await message.bot.get_file(message.document.file_id)
    file_path = file.file_path

    # cкачивание файла
    destination = f"resumes/{file_name}"
    await message.bot.download_file(file_path, destination)

    if file_name.lower().endswith(".pdf"):
        text = extract_text_from_pdf(destination)
    else:
        text = extract_text_from_docx(destination)

    if not text or text.strip() == "":
        await message.reply("Не удалось извлечь текст из файла. Пожалуйста, проверь, что файл содержит текст.")
        return

    # сохранение текста в памяти для дальнейшего парсинга
    await state.update_data(user_resume_text=text)

    await message.reply(text=text, parse_mode=None)
    await message.answer(text="Хочешь получить ключевые навыки, найденные в твоём резюме?", reply_markup=ikb.key_skills())

@router.callback_query(F.data == "yes")
async def accept_key_skills(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    # получение текста резюме из памяти
    data = await state.get_data()
    text = data["user_resume_text"]

    result = await async_http(
        method="POST",
        url="http://127.0.0.1:8000/resume/extract_skills",
        params={
            "text": text
        }
    )

    skills = result.get("skills", None)

    if skills:
        await callback.message.answer(f"✨ Найденные навыки: {', '.join(skills)}")
    else:
        await callback.message.answer("Навыков не найдено 🤔")

    await state.clear()

@router.callback_query(F.data == "no")
async def decline_key_skills(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Хорошо. Давай вернёмся в начало.")
    await state.clear()
    await user_text(callback.message)

# место хранения вакансий пользователей
user_vacancies = defaultdict(list)

# команда /search
@router.message(F.text == "💼 Вакансии")
@router.message(Command("search"))
async def search_command(message: Message):
    # генерация трёх вакансий
    vacancies = return_vacancies()

    # получение id пользователя - ключа для словаря
    user_id = message.from_user.id

    # сохранение текущих вакансий
    user_vacancies[user_id].append(vacancies)

    # добавление номера вакансии
    vacancy_text = "Вакансия #1\t" + vacancies[0]

    await message.answer(
        vacancy_text,
        disable_web_page_preview=True,
        reply_markup=ikb.vacancies(0, len(user_vacancies[user_id])-1)
    )

# навигация по вакансиям
@router.callback_query(F.data.startswith("vacancy:"))
async def navigate_vacancy(callback: CallbackQuery):
    # получение номера вакансии и номера набора вакансий
    idx, set_number = map(int, callback.data.split(":")[1:])

    # получение текста вакансии
    # добавление номера вакансии
    user_id = callback.from_user.id
    vacancy_text = f"Вакансия #{idx + 1}" + user_vacancies[user_id][set_number][idx]

    await callback.message.edit_text(
        vacancy_text,
        disable_web_page_preview=True,
        reply_markup=ikb.vacancies(idx, set_number)
    )
    await callback.answer()

# любое сообщение пользователя
@router.message(F.text)
async def user_text(message: Message):
    await message.answer("""Воспользуйся одной из кнопок чтобы перейти к возможностям бота:

/resume - отправь мне резюме и я подскажу что можно улучшить.
/search - покажу тебе подходящие вакансии и вместе решим куда лучше откликнуться.
""", reply_markup=rkb.start())