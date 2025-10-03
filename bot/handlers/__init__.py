import importlib
import pkgutil

from aiogram import Router

routers: list[Router] = []

for _, module_name, is_pkg in pkgutil.iter_modules(__path__):
    if not is_pkg:  # чтобы не заходить в подпапки
        module = importlib.import_module(f"{__name__}.{module_name}")
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, Router):
                routers.append(attr)