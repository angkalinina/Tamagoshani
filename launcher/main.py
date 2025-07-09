import argparse


def run_pygame():
    from bot.handlers.game import Game
    game = Game()
    game.run()


def run_bot():
    from launcher.main import main as run_telegram_bot
    run_telegram_bot()


def main():
    parser = argparse.ArgumentParser(description="Run Tamagoshani in different modes")
    parser.add_argument(
        "--mode",
        choices=["pygame", "bot"],
        default="pygame",
        help="Choose mode to run: 'pygame' for game UI or 'bot' for Telegram bot"
    )
    args = parser.parse_args()

    if args.mode == "bot":
        print("Starting Telegram bot...")
        run_bot()
    else:
        print("Starting Pygame interface...")
        run_pygame()


if __name__ == "__main__":
    main()
