import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

global choosen_cipher
choosen_cipher = ""

global user_message
user_message = ""

def caesar_cipher(text_message, shift):
   if shift != 0:
    print("Caesar works")


def number_cipher(text_message):
    pass

@bot.message_handler(commands=['start'])
def welcome(message):
    #sti = open('static/welcome.webp', 'rb')
    #bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Decoding")
    item2 = types.KeyboardButton("Encoding")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Hello there, {0.first_name}!\nMy name is - <b>{1.first_name}</b>, I will help you to secure your messages.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def main_loop(message):
    if message.chat.type == 'private':
        if message.text == 'Decoding':
            pass
        elif message.text == 'Encoding':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Caesar cipher", callback_data='caesar_cipher')
            item2 = types.InlineKeyboardButton("Number cipher", callback_data='number_cipher')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, "Ok, let\'s do it", reply_markup=markup)

        else:
            global user_message
            shift = 0
            if choosen_cipher == "caesar_cipher":
                if user_message == "":
                    user_message = message.text
                else:
                    shift = message.text
                caesar_cipher(user_message, shift)
            elif choosen_cipher == "number_cipher":
                bot.send_message(message.chat.id, "You choose Number")
            else:
                bot.send_message(message.chat.id, "Please choose something")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    user_message = ""
    try:
        if call.message:
            global choosen_cipher
            if call.data == 'caesar_cipher':
                choosen_cipher = "caesar_cipher"
            elif call.data == 'number_cipher':
                choosen_cipher = "number_cipher"

            bot.send_message(call.message.chat.id, "Please enter your message")

            # remove inline buttons
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #    reply_markup=None)

            # show alert
            #bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            #    text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)