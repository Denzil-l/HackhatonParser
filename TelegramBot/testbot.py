import telebot
import webbrowser
from telebot import types
import DataBaseConnect
import downloadPHOTO
bot = telebot.TeleBot('6154059495:AAH1iTt4wXoStdT0GF_WXHwyvrodJ7YWcKw')


query_24 = """
SELECT * FROM one_day_posts
"""
query_give = """
SELECT * FROM give_posts
"""
one_day_data = DataBaseConnect.select(query_24)
give_data = DataBaseConnect.select(query_give)

downloadPHOTO.make_photos(give_data,'C:/Users/den-s/OneDrive/Desktop/HackathonFinal/TelegramBot/Give_Images/')
downloadPHOTO.make_photos(one_day_data,'C:/Users/den-s/OneDrive/Desktop/HackathonFinal/TelegramBot/One_Day_images/')
print('Parser is ready ro work')



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Show posts for last 24 hours', callback_data='one_day_posts')
    button2 = types.InlineKeyboardButton('Show giv posts', callback_data='give_posts')
    markup.row(button1, button2)    
    bot.send_message(message.chat.id, 'Choose the option', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'one_day_posts':
        for index_one, i in enumerate(one_day_data):
            text = f'{i[1]}\n{i[2]}\n{i[4]}'
            media = []
            if len(i[3]) > 0:
                for index_two, j in enumerate(i[3]):
                    photo_path = f'C:/Users/den-s/OneDrive/Desktop/HackathonFinal/TelegramBot/One_Day_images/photo{index_one}{index_two}.jpg'
                    with open(photo_path, 'rb') as photo_file:
                        media.append(telebot.types.InputMediaPhoto(media=photo_file.read(), caption=text))
                bot.send_media_group(callback.message.chat.id, media)
            else:
                bot.send_message(callback.message.chat.id, text)
            markup = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton('Visit Website', url=i[5])
            markup.add(button)
            bot.send_message(callback.message.chat.id, 'Click the button below to visit the website:', reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Show posts for last 24 hours', callback_data='one_day_posts')
        button2 = types.InlineKeyboardButton('Show giv posts', callback_data='give_posts')
        markup.row(button1, button2)

        bot.send_message(callback.message.chat.id, 'Choose the option', reply_markup=markup)
    elif callback.data == 'give_posts':
        for index_one, i in enumerate(give_data):
            text = f'{i[1]}\n{i[2]}\n{i[4]}'
            media = []
            if len(i[3]) > 0:
                for index_two, j in enumerate(i[3]):
                    photo_path = f'C:/Users/den-s/OneDrive/Desktop/HackathonFinal/TelegramBot/Give_Images/photo{index_one}{index_two}.jpg'
                    with open(photo_path, 'rb') as photo_file:
                        media.append(telebot.types.InputMediaPhoto(media=photo_file.read(), caption=text))
                bot.send_media_group(callback.message.chat.id, media)
            else:
                bot.send_message(callback.message.chat.id, text)
            markup = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton('Facebook', url=i[5])
            markup.add(button)
            bot.send_message(callback.message.chat.id, 'Link to Facebook', reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Show posts for last 24 hours', callback_data='one_day_posts')
        button2 = types.InlineKeyboardButton('Show giv posts', callback_data='give_posts')
        markup.row(button1, button2)

        bot.send_message(callback.message.chat.id, 'Choose the option', reply_markup=markup)    
  

bot.polling(non_stop=True)

