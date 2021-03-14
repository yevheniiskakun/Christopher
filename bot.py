import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

delimiter = ","
key = '@~'

@bot.message_handler(commands=['start'])
def welcome(message):

  # keyboard
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


  bot.send_message(message.chat.id,
                   "Hi, {0.first_name}!\nMy name is - <b>{1.first_name}</b>, I will decode and encode your messages".format(
                     message.from_user, bot.get_me()),
                   parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def main(message):
  if message.chat.type == 'private':
    if key in message.text:
      message_before_decoding = message.text
      print("Decoding")
      message_list = list(message_before_decoding)

      bot.send_message(message.chat.id, str(message_list))
    else:
      print("Encoding")
      message_before_encoding = message.text
      message_list = list(message_before_encoding)


      bot.send_message(message.chat.id, str(message_list))




# RUN
bot.polling(none_stop=True)