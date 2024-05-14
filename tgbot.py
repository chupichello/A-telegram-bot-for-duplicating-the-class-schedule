import fitz
def pre():
    pdffile = "D:\python1/a.pdf"
    doc = fitz.open(pdffile)
    page = doc.load_page(0) # number of page
    pix = page.get_pixmap()
    output = "D:\python1/понедельник.png"
    pix.save(output)
    page = doc.load_page(1) # number of page
    pix = page.get_pixmap()
    output = "D:\python1/вторник.png"
    pix.save(output)
    page = doc.load_page(2) # number of page
    pix = page.get_pixmap()
    output = "D:\python1/среда.png"
    pix.save(output)
    page = doc.load_page(3) # number of page
    pix = page.get_pixmap()
    output = "D:\python1/четверг.png"
    pix.save(output)
    page = doc.load_page(4) # number of page
    pix = page.get_pixmap()
    output = "D:\python1/пятница.png"
    pix.save(output)
    doc.close()

import telebot
from telebot import types
API_KEY = '6726764476:AAEhfg1x8PNcKEJ2u1aUxudnNTJFsuFXcdg'
bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton("Понедельник")
    button2 = types.KeyboardButton("Вторник")
    button3 = types.KeyboardButton("Среда")
    button4 = types.KeyboardButton("Четверг")
    button5 = types.KeyboardButton("Пятница")

    markup.add(button1, button2, button3, button4, button5)

    bot.send_message(message.chat.id, \
                     "Здравствуйте, спасибо, что выбрали этот замечательный способ просмотра расписания. Удачного Вам просмотра!")
    bot.send_message(message.chat.id, "Выберите нужный день:", reply_markup=markup)
pre()

@bot.message_handler(func=lambda message: message.text == "Понедельник")
def send_image1(message):
    with open('D:\python1/понедельник.png', 'rb') as image:
        bot.send_message(message.chat.id, "Вот ваше расписание:)")
        bot.send_photo(message.chat.id, image)

@bot.message_handler(func=lambda message: message.text == "Вторник")
def send_image2(message):
    with open('D:\python1/вторник.png', 'rb') as image:
        bot.send_message(message.chat.id, "Вот ваше расписание:)")
        bot.send_photo(message.chat.id, image)

@bot.message_handler(func=lambda message: message.text == "Среда")
def send_image3(message):
    with open('D:\python1/среда.png', 'rb') as image:
        bot.send_message(message.chat.id, "Вот ваше расписание:)")
        bot.send_photo(message.chat.id, image)

@bot.message_handler(func=lambda message: message.text == "Четверг")
def send_image4(message):
    with open('D:\python1/четверг.png', 'rb') as image:
        bot.send_message(message.chat.id, "Вот ваше расписание:)")
        bot.send_photo(message.chat.id, image)

@bot.message_handler(func=lambda message: message.text == "Пятница")
def send_image5(message):
    with open('D:\python1/пятница.png', 'rb') as image:
        bot.send_message(message.chat.id, "Вот ваше расписание:)")
        bot.send_photo(message.chat.id, image)

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)