from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import random

default_probability = 100
boosted_probability = 100

known_nicknames = [
    "Сиссел",
    "Кей",
    "Гант",
    "Детектив",
    "Райт",
    "Вера"
]

# "У меня еще есть шансы попасть в серебро!"

idle_nothing = [
    "О Боже. Теперь о религии заговорили.",
    "Где мне найти соавтора для книги?",
    "*упражняется во владении посохом вращая его вокруг себя и перебирая из рук в руки*",
    "*радуется, что родился не во времена СССР*",
    "Оборачиваться в прошлое - все равно что там застрять в ущерб будущему.",
    "Я БОГ!!!",
    "Сегодня я на крыльях ветра.",
    "Так отвратительно обосрать классику это еще уметь надо.",
    "Зачем ехать в Питер, если ты не собираешься по нему гулять? Бессмыслица какая-то.",
    "*вздох* И почему я не удивлен?",
    "*до слёз*  😥"
]

league_of_legends = [
    "С читерами не разговариваю.",
    "Такие вещи не принято обсуждать, чтобы моральный дух не упал.",
    "Теперь моя жизнь в руинах... Путь в Лиге Легенд подошел к концу."
]

LOL_keywords = [
    "лол",
    "лолец",
    "Лига Легенд",
    "киберспорт"
]

social = [
    "Вы на сервер придете когда-нибудь, сычи?",
    "Ваша конфа не крута и не раскручена.",
    "Дерьмо ваш Твиттер.",
    "Подписывайтесь на мой канал: https://www.youtube.com/channel/UCK_k975KbZNL8fBF-p0cr8w Только качественный контент!",
    "Это среди вас больные мозгом ставят мне дизлайки?! Расстреляю!"
]

social_keywords = [
    "Вконтакте",
    "контакт",
    "Твиттер",
    "твитор",
    "Ютуб",
    "ютруп",
    "фикбук",
    "сервер",
    "атторни онлайн",
    "лайк"
]

personal = [
    "Слушай меня, дурень: you suck.",
    "Чума на твою голову, bastardo!",
    "Да пошел ты, (username)!",
    "*достал дробовик и расстрелял (username)*",
    "(username), ты вообще ничего толкового предложить не можешь! Уйди восвояси!",
    "(username)!!! ВЕРНИСЬ!!! Я ВСЕ ПРОЩУ!!! ПОЖАЛУЙСТА!!!",
    "(username), чтоб тебя навечно забанили! Везде!",
    "Но ведь (username) - белорус.",
    "Ты говоришь несуразную чушь сейчас. Это ты в данный момент ведешь себя, как на голову отшибленный.",
    "У меня щас из за тебя перегрузка системы будет. Прекрати своим трояном вирусить."
]

personal_keywords = [
    "Польк",
    "Полли",
    "Аполло",
    "глуп",
    "Беларус",
    "Белорусси"
]

BNM = [
    "Прерывать мои мысли своими - крайне невежливо!",
    "Порой вы такие странные, что ужас дикий.",
    "Вы вообще люди или просто кучка гиен?",
    "Какого фига вы не спите?! Вы тут своими сообщениями спать мешайте!",
    "Эй! Вы на что намекайте?",
    "Завистники!",
    "Не было у меня такомобиля!",
    "Вы опять все тут упоролись что ли?!",
    "Кругом одни предатели, никому нельзя довериться!",
    "Да вы издевайтесь!",
    "Это просто недопустимо! ****!",
    "Deploy the nukes! *спрятался в бункере*",
    "*достал дробан* Живо прекращай эту упоротость!",
    "JUST DO IT YOURSELF DAMN IT!",
    "Вы сами дали повод на вас выругаться.",
    "Еще одна тупая шутка - и вам не жить.",
    "*достал автоматы* Массовые расстрелы спасут мир!",
]

BNM_keywords = [
    "такомобиль",
    "бугурт",
    "дело"
]

Levap_table_1 = {}
Levap_table_2 = {}
Levap_table_1["LOL"] = league_of_legends
Levap_table_2["LOL"] = LOL_keywords
Levap_table_1["social"] = social
Levap_table_2["social"] = social_keywords
Levap_table_1["personal"] = personal
Levap_table_2["personal"] = personal_keywords
Levap_table_1["BNM"] = BNM
Levap_table_2["BNM"] = BNM_keywords

Levap_replica = []
for replica in idle_nothing:
    Levap_replica.append(replica)
for replica in league_of_legends:
    Levap_replica.append(replica)
for replica in social:
    Levap_replica.append(replica)
for replica in personal:
    Levap_replica.append(replica)
for replica in BNM:
    Levap_replica.append(replica)

def reply(bot, update):
    a = random.randint(0,99) # на будущее: да, Сис, значение 99 здесь достижимо, верхняя граница включительна.
    #update.message.reply_text(str(a))
    probability = default_probability
    response = "(default)" # Levap_replica[random.randint(0,len(Levap_replica))]
    for key in Levap_table_1.keys():
        for keyword in Levap_table_2[key]:
            if keyword in update.message.text:
                probability = boosted_probability
                selected_set = Levap_table_1[key]
                response = selected_set[random.randint(0,len(selected_set))]
                break
        else:
            break
    if response == "(default)":
        response = idle_nothing[random.randint(0, len(idle_nothing))]
    if "(username)" in response:
        response = response.replace("(username)",known_nicknames[random.randint(0,len(known_nicknames))]) # update.message.from_user.username
    # if a < probability:
    chat_id = update.message.chat.id
    sendMessage(chat_id, response)
    # update.message.reply_text(responce, quote=False)

updater = Updater('829807051:AAGwMUS5eAvJ15xKIOwMdbmbGr_MUosg7Wo')

updater.dispatcher.add_handler(MessageHandler(Filters.all, reply))

updater.start_polling()
updater.idle()
