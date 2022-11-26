import telebot  # user=MY_QAP_BOT; username=my_qap_bot

bot = telebot.TeleBot("5939572755:AAH7uVI6j4uJMFtFAfzHXIElmJLOYhGzURg")


@bot.message_handler(content_types=['voice'])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Hi! Nice to hear you!")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}!")


@bot.message_handler(content_types=['sticker'])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme, dude!')


bot.polling(none_stop=True)
