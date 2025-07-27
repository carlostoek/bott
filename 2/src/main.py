from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.executor import start_polling

from config import BOT_TOKEN
from handlers.start_handler import register_start_handler

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Inicia el bot")
    ]
    await bot.set_my_commands(commands)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    register_start_handler(dp)

    await set_commands(bot)
    await start_polling(dp, bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())