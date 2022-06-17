from telegram import Update
from telegram.ext import Updater, Filters, MessageHandler, CallbackContext
import random
import list_provider

default_probability = 20
boosted_probability = 80


def universal_reply(msg_text):
    a = random.randint(0, 99)
    probability = default_probability
    response = "(default)"
    lines_dict = list_provider.get_lines_dict()
    keywords_dict = list_provider.get_keywords_dict()
    for key in lines_dict.keys():
        for keyword in keywords_dict[key]:
            if keyword in msg_text.lower():
                probability = boosted_probability
                selected_set = lines_dict[key]
                response = selected_set[random.randint(0, len(selected_set) - 1)]
                break
        if response != "(default)":
            break
    if response == "(default)":
        idle_lines = list_provider.get_idle()
        response = idle_lines[random.randint(0, len(idle_lines) - 1)]
    if "(username)" in response:
        known_nicknames = list_provider.get_known_nicknames()
        response = response.replace("(username)", known_nicknames[random.randint(0, len(known_nicknames) - 1)])
    return (a < probability), response


def telegram_reply(update: Update, context: CallbackContext):
    msg_text = ""
    if update.message is not None:
        msg_text = update.message.text
    success, response = universal_reply(msg_text)
    if success:
        context.bot.send_message(update.effective_chat.id, response)


updater = Updater('829807051:AAGwMUS5eAvJ15xKIOwMdbmbGr_MUosg7Wo', use_context=True)

updater.dispatcher.add_handler(MessageHandler(Filters.all, Telegram_reply))

updater.start_polling()
updater.idle()
