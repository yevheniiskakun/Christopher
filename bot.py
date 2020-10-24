import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

def caesar_cipher(text_message, shift):
    pass

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
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Decoding':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == 'Encoding':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Caesar cipher", callback_data='caesar_cipher')
            item2 = types.InlineKeyboardButton("Number cipher", callback_data='number_cipher')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, "Ok, let\'s do it", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Please choose something')
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    user_message = ""
    try:
        if call.message:
            bot.send_message(call.message.chat.id, 'Please enter the text message')
            if call.data == 'caesar_cipher':
                pass
            elif call.data == 'number_cipher':
                pass

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