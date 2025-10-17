import os

history=[]

def handle_action(bot, message):
    '''Реакция на кнопку погладить кота'''
    text = message.text

    if 'Погладить' in text:
        history.append('Погладить кота')
        photo_path = os.path.join('media', 'cat_2.jpg')
        if os.path.exists(photo_path):
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=" Погладить кота")
    elif 'Обнять' in text:
        history.append('Обнять кота')
        photo_path = os.path.join('media', 'cat.jpg')
        if os.path.exists(photo_path):
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=" Обнять кота")