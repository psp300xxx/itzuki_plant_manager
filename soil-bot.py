import RPi.GPIO as GPIO
import time
import telepot
from general_information import ProjectConstants
CONSTANTS = ProjectConstants.ProjectConstant
from telepot.loop import MessageLoop

messaggio = ""

#GPIO SETUP
channel = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

TOKEN = "" # token del bot

bot = telepot.Bot(TOKEN)
id_itzuki = "" # id di Telegram (numerico)

# rewritten in raspberry package
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

    # Avoid the use of if elif structures, it's better to leverage on design patterns
    # In this case I would create a class structure having the logic for each commands
    # In this way, in case you want to add multiple input parameters your code would not explode
    if command == '/start':
        # Avoid using magic variables like "Ciao sono la tua piantina" in this case
        # create a structure like an enum having this information
        bot.sendMessage(chat_id, CONSTANTS.HELLO_MESSAGE)

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

# Integrate methods in the middle object
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # se il pin va HIGH o LOW
GPIO.add_event_callback(channel, callback)  # invoca la funzione quando il pin cambia

# Avoid doing busy waiting, this will make you waste CPU-time for multithread/multiprocess apps
# However, in this case this can still be the correct choice, I am not an expert in Raspberry programming.
while True:
    time.sleep(10)
