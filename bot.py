import telebot
import random, os
# import datetime
# import pytz


TOKEN ='1756123183:AAFjCiddoo8IiWy4xrqq7ebFrZcuzEYbbLw'
# TIMEZONE = 'Europe/Kiev'

# P_TIMEZONE = pytz.timezone(TIMEZONE)

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start','pic','meme','cursed'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "to get wholesome smth, type /pic\n/meme is for memes")
    elif message.text == "/pic":
        directory = "!!pics"
        random_image = random.choice(os.listdir(directory))
        with open ("!!pics"+"/"+ random_image, "rb") as file:
            bot.send_photo(message.from_user.id, photo = file)
    elif message.text == "/meme":
        directory = "!!memes"
        random_image = random.choice(os.listdir(directory))
        with open ("!!memes"+"/"+ random_image, "rb") as file:
            bot.send_photo(message.from_user.id, photo = file)
    elif message.text == "/cursed":
    directory = "!!cursed"
    random_image = random.choice(os.listdir(directory))
    with open ("!!cursed"+"/"+ random_image, "rb") as file:
        bot.send_photo(message.from_user.id, photo = file)
    else:
        bot.send_message(message.from_user.id, 'no :/')
            
    
        
bot.polling(none_stop=True)
