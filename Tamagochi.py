import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class Tamagotchi:
    def __init__(self):
        self.happiness = 100
        self.hunger = 100

    def feed(self):
        self.hunger += 10
        if self.hunger > 100:
            self.hunger = 100

    def play(self):
        self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100

    def update(self):
        self.hunger -= 0.1
        self.happiness -= 0.1

        if self.hunger < 0:
            self.hunger = 0
        if self.happiness < 0:
            self.happiness = 0

# Хранение состояния тамагочи для каждого пользователя
user_tamagotchis = {}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я твой Тамагочи. Используй /feed для кормления и /play для игры.')

def feed(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    tamagotchi = user_tamagotchis.get(user_id, Tamagotchi())
    tamagotchi.feed()
    user_tamagotchis[user_id] = tamagotchi
    update.message.reply_text(f'Ты покормил своего Тамагочи! Уровень голода: {tamagotchi.hunger}')

def play(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    tamagotchi = user_tamagotchis.get(user_id, Tamagotchi())
    tamagotchi.play()
    user_tamagotchis[user_id] = tamagotchi
    update.message.reply_text(f'Ты поиграл с своим Тамагочи! Уровень счастья: {tamagotchi.happiness}')

def status(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    tamagotchi = user_tamagotchis.get(user_id, Tamagotchi())
    tamagotchi.update()
    update.message.reply_text(f'Уровень голода: {tamagotchi.hunger}, Уровень счастья: {tamagotchi.happiness}')

def main() -> None:
    # Вставьте свой токен здесь
    updater = Updater("7330806591:AAHKoWSIlcEleK8yit8sxJQ-Jr-oD_BcJPo")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("feed", feed))
    dispatcher.add_handler(CommandHandler("play", play))
    dispatcher.add_handler(CommandHandler("status", status))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
