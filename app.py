import telebot
from config import keys, TOKEN
from extensions import CurrencyConverter, APIException


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующе формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values_ = message.text.split(' ')
        if len(values_) != 3:
            raise APIException('Некорректное количество параметров.')
        quote, base, amount = values_
        total_base = CurrencyConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        f = CurrencyConverter.useless_fact(amount)
        text = f'Цена {amount} {quote} в {base} - {float(total_base) * int(amount)}\n\
Кстати, ненужный факт про {amount} (ин инглиш): {f}'
        bot.send_message(message.chat.id, text)


bot.polling()
