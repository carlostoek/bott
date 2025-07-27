from aiogram.types import Message

async def start_command_handler(message: Message):
    """
    Handle the /start command by sending a greeting message.
    """
    await message.answer("¡Hola! Bienvenido al bot de Telegram.")