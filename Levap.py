from telegram import Update
from telegram.ext import Updater, Filters, MessageHandler, CallbackContext
import random

default_probability = 20
boosted_probability = 80

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
    "*до слёз*  😥",
	"Argument of silly hater, who understand nothing about it.",
    "Привет. Поговорим в лс?",
	"О! Ещё в игнор ушли как последний трус. Прелестно...",
	"Хммм, занимательно."
]

league_of_legends = [
    "С читерами не разговариваю.",
    "Такие вещи не принято обсуждать, чтобы моральный дух не упал.",
    "Теперь моя жизнь в руинах... Путь в Лиге Легенд подошел к концу."
]

LOL_keywords = [
    "лол",
    "лига легенд",
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
    "вконтакте",
    "контакт",
    "твиттер",
    "твитор",
    "ютуб",
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
    "У меня щас из за тебя перегрузка системы будет. Прекрати своим трояном вирусить.",
    "Ты за идиота меня принимаешь? Левап - не тиран!",
    "Это отсылка на политические события в Беларуси? Ты там совсем больной, (username)?!",
    "Больше не показывай мне эту хрень и сотри к чёрту.",
    "Ты прекратишь наконец эту детскую глупость??? Вы что там себе позволяйте?!",
    "А тебе какое к чёрту дело, (username)?",
    "Ну и кто тут после этого ребёнок с такими доводами? Это вы первыми начали этот абсурд. Не я.",
    "Вам просто нечем заняться. Вот и лезете не в своё дело!",
    "Вот уж не думал, что (username) и тебе подобные опустишься до подобного уровня. И всё это из за моих личных дел, которые никак вас на касаются.",
    "Мне нечего отвечать ребёнку, который даже не мог ответить на МОЙ вопрос.",
    "Неужели? Откуда мне знать что это не всего лишь твои пустые громкие слова?",
    "Ты так и будешь дальше валять дурака, (username)? Я думал у нас серьёзный разговор.",
    "Ты серьёзно? В жизни не слышал подобного фарса.",
    "Ты понимаешь что этим переступаешь все этические черты?",
    "В данный момент - ты сейчас ничем не лучше.",
    "Ты хочешь мне сказать, что я заставлял что-то делать? Ты в своём уме, (username)?",
    "Ты сейчас используешь слова человека по имени \"(username)\", которому давно уже не интересно вести дела со мной.",
    "Ты сейчас коверкаешь мои слова, (username).",
	"Ты что творишь, (username)? Охренел?",
	"Сразу видно отбитый на голову, раз занимаешься подобной дичью как маленький ребёнок!",
	"Ты явно не в себе, раз позволяешь себе подобное."
]

personal_keywords = [
    "польк",
    "полли",
    "аполло",
    "глуп",
    "беларус",
    "белорусси",
    "левап",
    "тиран",
    "диктатор",
    "гитлер",
    "ребёнок",
    "ребёнк",
    "шлейк",
    "шлеек",
    "шлюх",
    "порно"
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
    "Что это за наркомания? Это даже не смешно.",
    "Низко. Очень низко.",
    "А какое вам дело? По вашему я сделал что-то плохое?",
    "Попрошу убрать свой любопытный нос подальше.",
	"Да вы все уже там такие, после того как покинули Attorney Online.",
	"Опять ваши фантазии без почвы..."
]

BNM_keywords = [
    "такомобил",
    "бугурт",
    " дел",
    "дурак",
    "дурк",
    "дурень",
    "торчок",
    "торчк",
    "идиот",
    "пидор"
]

pidor = [
    "О, прелестно! Мы еще будем мериться мужскими стволами?",
    "Может, скажу скажешь, что сын олигарха? А? Зажрался!",
    "Даже поганные ниггеры и то лучше вас.",
    "I don't like them putting chemicals in the water, THEY TURN THE FREAKING FROGS GAY!",
    "Я не знаю, кто такой Федя, но он как-то с этим связан!"
]

pidor_keywords = [
    "pidor"
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

#Levap_replica = []
#for replica in idle_nothing:
#    Levap_replica.append(replica)
#for replica in league_of_legends:
#    Levap_replica.append(replica)
#for replica in social:
#    Levap_replica.append(replica)
#for replica in personal:
#    Levap_replica.append(replica)
#for replica in BNM:
#    Levap_replica.append(replica)

def universal_reply(msgtext):
    a = random.randint(0,99) # на будущее: да, Сис, значение 99 здесь достижимо, верхняя граница включительна.
    #update.message.reply_text(str(a))
    probability = default_probability
    response = "(default)" # Levap_replica[random.randint(0,len(Levap_replica))]
    for key in Levap_table_1.keys():
        for keyword in Levap_table_2[key]:
            if keyword in msgtext.lower():
                probability = boosted_probability
                selected_set = Levap_table_1[key]
                response = selected_set[random.randint(0,len(selected_set) - 1)]
                break
        if response != "(default)":
            break
    if response == "(default)":
        response = idle_nothing[random.randint(0, len(idle_nothing) - 1)]
    if "(username)" in response:
        response = response.replace("(username)", known_nicknames[random.randint(0,len(known_nicknames) - 1)]) # update.message.from_user.username
    return (a < probability), response

def Telegram_reply(update: Update, context: CallbackContext):
    msgtext = ""
    if update.message is not None:
        msgtext = update.message.text
    success, response = universal_reply(msgtext)
    if success:
        update.message.reply_text(response, quote=False)
    #chat_id = update.message.chat.id
    #bot.send_message(chat_id, response)


updater = Updater('829807051:AAGwMUS5eAvJ15xKIOwMdbmbGr_MUosg7Wo', use_context=True)

updater.dispatcher.add_handler(MessageHandler(Filters.all, Telegram_reply))

updater.start_polling()
updater.idle()
