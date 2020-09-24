import telebot
from pyowm import OWM
import requests


owm = OWM('650b6226d880752836b402f320040f66')
bot = telebot.TeleBot("1377245085:AAFrjEwTAqN1vc8Ni2ULF58zhRlhbdj3uzg")
def get_location_info():
    return requests.get("http://ip-api.com/json/").json()

@bot.message_handler(content_types=['text'])
def echo_all(message):
	#bot.reply_to(message, message.text)
    #bot.send_message(message.chat.id, message.text)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather

    # Weather details
    answer= "Сейчас в" +" " + message.text+ "\n"
    answer+="Скорость ветра:"+" "+str(w.wind()["speed"])+"m/s"+"\n"
    answer+="Влажность:"+" "+str(w.humidity)+"%"+"\n"
    answer+="Температура:" +" "+str(w.temperature('celsius')["temp"])+" "+"градусов цельсия"+"\n"
    answer+= "\n"
    answer+= "Ваш адрес:"+" "+str(get_location_info()["city"])+"\n"
    answer+= "Ваша временная зона:"+" "+str(get_location_info()["timezone"])+"\n"
    answer+= "Ваши координаты:"+" "+str(get_location_info()["lat"])+" "+str(get_location_info()["lon"])+"\n"
    answer+= "Ваш IP:"+" "+str(get_location_info()["query"])+"\n"

    bot.send_message(message.chat.id,answer)


bot.polling()
