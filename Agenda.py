import telepot
from Storage import *
from telepot import Bot,glance
from telepot.loop import MessageLoop
from time import sleep

bot = Bot('942673543:AAG3pv-LNCNDrlituhImluCyiCnVcnPsyPE')

def onChatMessage(msg):
    content_type,chat_type,chat_id, = glance(msg)
    if content_type == 'text':
        command = msg['text']
        if '/start' in command:
            sendMessage(chat_id,f'Olá seja bem vindo *{msg["from"]["first_name"]}*')
        elif '/list' in command:
            sendMessage(chat_id, getAlertList(str(chat_id),users))
        elif '/alert' in command:
            command = command[6:]
            message,day,hour = command.split(' % ')
            alert = createAlert(message,day,hour)
            updateAlert(chat_id,users,alert)
            updateFile(users)
            sendMessage(chat_id, f'Lembrete ativado*{msg["from"]["first_name"]}*')

def sendMessage(chat_id, text):
    bot.sendChatAction(chat_id, 'typing')
    sleep(1)
    bot.sendMessage(chat_id,text, parse_mode='Markdown')



users = loadFile()

print(bot.getMe())
MessageLoop(bot, onChatMessage).run_as_thread()

while True:
    pass