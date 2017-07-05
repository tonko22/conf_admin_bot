import config
import telebot
import time

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def send_photo(message):
    print(message)
    if message.text == 'gogogo':
        text = "Быстрее втаривай пиво"
        bot.send_message(config.channel_name, text)


 # Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['photo'])
def add_photo_to_archive(message):
    file_id = message.photo[0].file_id
    print('File id: ', file_id)
    # file_path = bot.get_file(file_id).file_path
    # bot.send_photo(config.channel_name, file_id, caption=text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
