from .actions import history

def show_history(bot, message):
    '''отображение истории'''

    if history:
        bot.send_message(message.chat.id, '\n'.join(history))
    else:
        bot.send_message(message.chat.id, 'нет истории')
