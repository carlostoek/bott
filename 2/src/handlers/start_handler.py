from aiogram import Dispatcher
from aiogram.types import Message

async def start_command_handler(message: Message):
    await message.answer("¡Hola! Bienvenido al bot de Telegram.")

def register_start_handler(dp: Dispatcher):
    dp.message.register(start_command_handler, commands={"start"})