"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import settings
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
#    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME, 
        'password': settings.PROXY_PASSWORD
    }
}


def constellation(my_planet):
    today = datetime.datetime.now().strftime("%Y/%m/%d")
    try:
        _, constellation_name = ephem.constellation(getattr(ephem, my_planet)(today))
    except AttributeError:
        return 'Неверно введено название планеты'
    return  f'Планета {my_planet} находится сегодня в созвездии: {constellation_name}'
    


def greet_user(update, context):
    text = 'Вызван /start'
    logging.info("Команда /start")
    update.message.reply_text(f'Привет, пользователь: {update.message.from_user.username}! \nУкажите планету по которой хотите получить информацию.')

   
def planet_info(update, context):
    text = 'Вызван /planet'
    logging.info("Команда /planet")
    _, my_planet = update.message.text.split()
    update.message.reply_text(constellation(my_planet))


def talk_to_me(update, context):
    user_text = update.message.text
    logging.info("Зеркальное сообщение")
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал!")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
