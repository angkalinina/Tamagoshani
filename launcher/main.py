import argparse
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from bot.handlers import game  # Telegram команды

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


def run_pygame():
    from bot.handlers.game import Game
    game = Game()
    game.run()


async def run_bot():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(game.router)
    print("Telegram bot started")
    await dp.start_polling(bot)


def main():
    parser = argparse.ArgumentParser(description="Run Tamagoshani in different modes")
    parser.add_argument(
        "--mode", choices=["pygame", "bot"], default="pygame",
        help="Choose mode to run: 'pygame' for game UI or 'bot' for Telegram bot"
    )
    args = parser.parse_args()

    if args.mode == "bot":
        print("Starting Telegram bot...")
        asyncio.run(run_bot())
    else:
        print("Starting Pygame interface...")
        run_pygame()


if __name__ == "__main__":
    main()
