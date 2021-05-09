import telebot
import random, os
# import datetime
# import pytz


TOKEN ='1756123183:AAFjCiddoo8IiWy4xrqq7ebFrZcuzEYbbLw'
# TIMEZONE = 'Europe/Kiev'

# P_TIMEZONE = pytz.timezone(TIMEZONE)

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start','pic'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "to get wholesome, type /pic")
    elif message.text == "/pic":
        bot.send_message(message.from_user.id, "there have to be a picture :/")
        #directory = "D:\z pic folder"
        #random_image = random.choice(os.listdir(directory))
        #with open ("D:\z pic folder"+"\\"+ random_image, "rb") as file:
        #    bot.send_photo(message.from_user.id, photo = file)
    else:
        bot.send_message(message.from_user.id, ':/')
            
    
        
bot.polling(none_stop=True)
