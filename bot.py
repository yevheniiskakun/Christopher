import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

delimiter = ","
keys = ['@~']

ascii_key = "@~"

final_message = ""


def ascii_decoder(message):
  decoded_message = ""
  message_before_decoding = message.replace(ascii_key, "")
  message_before_decoding_list = message_before_decoding.split(delimiter)
  for i in message_before_decoding_list:
    if i != "":
      part = str(chr(int(i))) + ""
      decoded_message += part
  global final_message
  final_message = str(decoded_message)


def ascii_encoder(message):
  encoded_message = ""
  for i in message:
    part = str(ord(i)) + delimiter
    encoded_message += part
  encoded_message = str(ascii_key + encoded_message)
  global final_message
  final_message = str(encoded_message)


@bot.message_handler(commands=['start'])
def welcome(message):

  # keyboard
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button1 = types.KeyboardButton("Test encoding")
  button2 = types.KeyboardButton("@~84,104,105,115,32,105,115,32,97,32,100,101,99,111,100,105,110,103,")

  markup.add(button1, button2)

  bot.send_message(message.chat.id,
                   "Hi, {0.first_name}!\nMy name is - <b>{1.first_name}</b>, I will decode and encode your messages. You can it see how it works by pressing the buttons below".format(
                     message.from_user, bot.get_me()),
                   parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def main(message):
  if message.chat.type == 'private':
    if any(word in message.text for word in keys):
      #print("Decoding")
      if ascii_key in message.text:
        message_before_decoding = message.text
        ascii_decoder(message_before_decoding)

    else:
      #print("Encoding")
      message_before_encoding = message.text
      ascii_encoder(message_before_encoding)

    bot.send_message(message.chat.id, final_message)


# RUN
bot.polling(none_stop=True)