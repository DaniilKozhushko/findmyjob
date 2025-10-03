import random
from typing import Optional, Literal
import aiohttp
import asyncio

async def async_http(
    url: str,
    method: Literal["GET", "POST"] = "GET",
    params: Optional[dict] = None,
    headers: Optional[dict] = None,
    timeout_sec: int = 10
):
    """
    Базовая функция для асинхронного HTTP-запроса.

    :param url: URL API
    :param method: HTTP метод ("GET" или "POST"), по умолчанию "GET"
    :param params: словарь параметров запроса, необязательный
    :param headers: словарь заголовков, необязательный
    :param timeout_sec: таймаут запроса в секундах
    :return: JSON-ответ сервера
    :raises Exception: если запрос завершился с ошибкой
    """
    timeout = aiohttp.ClientTimeout(total=timeout_sec)
    retries = 4
    min_delay = 1
    max_delay = 10
    factor = 2.7
    jitter = 0.1
    delay = min_delay

    for attempt in range(retries + 1):
        try:
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.request(
                    method=method,
                    url=url,
                    params=params if method == "GET" else None,
                    json=params if method == "POST" else None,
                    headers=headers if headers else None
                ) as response:
                    response.raise_for_status() # выбрасывание исключения для статуса >=400
                    return await response.json()
        except aiohttp.ContentTypeError:
            text = await response.text()
            raise Exception(f"Не JSON ответ от {url}: {text}")
        except aiohttp.ClientResponseError as e:
            if attempt == retries:
                raise Exception(f"HTTP ошибка {e.status} при запросе {url}")
        except aiohttp.ClientError as e:
            if attempt == retries:
                raise Exception(f"Ошибка запроса {url}: {str(e)}")

        # экспоненциальный бэкофф
        delay = delay * factor
        delay += random.uniform(0, jitter) * delay
        delay = min(delay, max_delay)
        await asyncio.sleep(delay)