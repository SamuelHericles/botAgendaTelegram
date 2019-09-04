import json

FILE_NAME = 'users.json'

def loadFile():
    from os.path import isfile
    if isfile(FILE_NAME):
        arq = open(FILE_NAME,'r')
        file = json.load(arq)
        arq.close()
        return file
    else:
        return dict()

def updateFile(users):
    arq = open(FILE_NAME,'w')
    json.dump(users, arq, indent=4)
    arq.close()

def createAlert(message,day,hour):
    return {
        'messge':message,
        'day': day,
        'hour': hour,
        'enable': True
    }

def getAlertList(chat_id,users):
    if chat_id not in users:
        return 'Não há nenhum lembre seu na minha base,seu lindo'
    users = users[chat_id]
    lst = 'Lista:\n'
    for alert in users:
        if alert['enabled']:
            lst += f'->*{alert["message"]}* -' \
                   f'{alert["day"]} às ' \
                   f'{alert["hour"]}'

    return lst