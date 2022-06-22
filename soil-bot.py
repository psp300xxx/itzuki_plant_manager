import RPi.GPIO as GPIO
import time
import telepot
from telepot.loop import MessageLoop

messaggio = ""

#GPIO SETUP
channel = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

TOKEN = "" # token del bot

bot = telepot.Bot(TOKEN)
id_itzuki = "" # id di Telegram (numerico)

def callback(channel):
    global messaggio
    if GPIO.input(channel):
        messaggio = "Mi sento asciutta, prova ad annaffiarmi"
    else:
        messaggio = "Mi sento annaffiata"
    print(messaggio)
    bot.sendMessage(id_itzuki, messaggio)
    return messaggio
callback(channel)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Ricevuto comando: %s' % command)

    if command == '/start':
        bot.sendMessage(chat_id, "Ciao sono la tua piantina")

    elif command == '/suolo' or command == '/suolo@piant_bot':
        try:
            callback(channel)
            if chat_id != id_itzuki:
                bot.sendMessage(chat_id, messaggio)
        except Exception as e:
            print(e)
            pass

bot.message_loop(handle)
print ('Listening ...')

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # se il pin va HIGH o LOW
GPIO.add_event_callback(channel, callback)  # invoca la funzione quando il pin cambia

while 1:
    time.sleep(10)
