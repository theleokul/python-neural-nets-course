from telebot import TeleBot, types
import zodiac as z


# To run this bot:
# 1. install pyTelegramBotAPI
# 2. run command in the terminal (with Anaconda prompt, where pyTelegramBotAPI is installed): python zodiac_telegram_bot.py
# 3. if no error occurs give your bot some commands to check its functionality


bot = TeleBot('PASTE_TOKEN_FROM_BOT_FATHER_HERE')


def show_zodiac_buttons_on(message):
    # Готовим кнопки
    keyboard = types.InlineKeyboardMarkup()

    for zod in z.zods:
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_zod = types.InlineKeyboardButton(text=zod, callback_data='zodiac')
        # И добавляем кнопку на экран
        keyboard.add(key_zod)

    # Показываем все кнопки сразу и пишем сообщение о выборе
    bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "\\hello":
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
        show_zodiac_buttons_on(message)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши \\hello")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac":
        # Формируем гороскоп
        msg = z.get_prediction()
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)


bot.polling(none_stop=True, interval=0)
