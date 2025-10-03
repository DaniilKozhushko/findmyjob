# FindMyJob
Telegram-бот для поиска вакансий, анализа резюме и извлечения ключевых навыков.
Проект написан на Python с использованием aiogram 3 для Telegram-бота и FastAPI для REST API.

## ⭐️ Основные функции

- Загрузка резюме
Пользователь может отправить PDF или DOCX файл с резюме.
Бот извлекает текст и сохраняет его для дальнейшего анализа.

- Извлечение ключевых навыков
После обработки резюме бот предлагает пользователю получить ключевые навыки.
Навыки извлекаются с помощью FastAPI-эндпоинта POST /resume/extract_skills.

- Встроенная клавиатура для взаимодействия

- Inline-кнопки для подтверждения извлечения ключевых навыков (Да / No).

- Простое взаимодействие через кнопки без необходимости писать команды.

## 🗂 Структура проекта
```
app/ # FastApi
├── routers/ # Роутеры
│   └── user_router.py # Роутер для пользователей
├── main.py # Точка входа
└── models.py # Классы, схемы, модели
bot/ # Telegram бот
├── handlers/ # Хэндлеры бота
│   └── user_router.py # Роутер с логикой и командами для пользователей
├── keyboards/ # Клавиатуры для бота
│   ├── inline.py # Inline-клавиатуры
│   └── reply.py # Reply-клавиатуры
├── middlewares/ # Промежуточные слои
│   └── clear_state.py # Автоматическая очистка Состояний
├── resumes # Директория для сохранения резюме польщователей
└── main.py # Точка входа
utils/ # Вспомогательные функции
├── utils # Синхронные
└── async_utils # Асинхронные
.env # Переменные окружения
.gitignore # Файлы и папки исключённые из поля зрения гита
config.py # Подключение переменных из .env
README.md # Описание проекта
requirements.txt # Перечень зависимостей
```

## Загрузка и запуск

1. Клонируй репозиторий:

   ```bash
   git clone https://github.com/DaniilKozhushko/findmyjob.git
   ```
   
   ```bash
   cd findmyjob
   ```

2. Создай .env файл:

   ```bash
   nano .env
   ```

   ```env
   TELEGRAM_BOT_TOKEN=telegram_bot_token
   ```
   
3. Создай и активируй виртуальное окружение:

   ```bash
   python3 -m venv venv
   ```

   ```bash
   source venv/bin/activate
   ```

4. Установи зависимости:

   ```bash
   pip install -r requirements.txt
   ```
   
5. Запусти:

   ```bash
    tmux new -s fastapi 
   ```

   ```bash
   source venv/bin/activate
   ```

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
   
   ```bash
   tmux new -s telegram_bot
   ```
   
   ```bash
   source venv/bin/activate
   ```
   
   ```bash
   python bot/main.py
   ```