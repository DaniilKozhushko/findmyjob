from aiogram.types import Message
from aiogram import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable
from aiogram.fsm.context import FSMContext

class AutoClearStateMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        state: FSMContext = data.get("state")

        if event.text and (event.text.startswith("/") or event.text in ["💼 Вакансии", "📄 Загрузить резюме"]):
            state: FSMContext = data.get("state")
            if state:
                await state.clear()

        return await handler(event, data)