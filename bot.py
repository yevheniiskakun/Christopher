import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):

  # keyboard

  bot.send_message(message.chat.id,
                   "Hello there, {0.first_name}!\nЯ - <b>{1.first_name}</b>, i'm here to encrypt and decode your messages.".format(
                     message.from_user, bot.get_me()),
                   parse_mode='html')


@bot.message_handler(content_types=['text'])
def lalala(message):
  if message.chat.type == 'private':
    if message.text != "":
      markup = types.InlineKeyboardMarkup(row_width=2)
      item1 = types.InlineKeyboardButton("Decode", callback_data='decode')
      item2 = types.InlineKeyboardButton("Encrypt", callback_data='encrypt')

      markup.add(item1, item2)

      bot.send_message(message.chat.id, 'Nice, what you choose?', reply_markup=markup)
    else:
      bot.send_message(message.chat.id, 'Please write something')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  try:
    if call.message:
      if call.data == 'decode':
        bot.send_message(call.message.chat.id, 'Please enter the message code')
      elif call.data == 'encrypt':


        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Caeser cipher", callback_data='caeser_cipher')
        item2 = types.InlineKeyboardButton("Number cipher", callback_data='number_cipher')

        markup.add(item1, item2)
        bot.send_message(call.message.chat.id, 'Please choose type of encryption', reply_markup=markup)
        
  except Exception as e:
    print(repr(e))


# RUN
bot.polling(none_stop=True)