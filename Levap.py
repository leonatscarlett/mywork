#!/usr/bin/env python3.4

import os

import sys

import config

import db

import datetime


from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import random

Levap_replica = ["Да вы издевайтесь!",
                 "Не было у меня такомобиля!",
                 "Вы опять все тут упоролись что ли?!",
                 "Да пошел ты, Гант!",
                 "Ваша конфа не крута и не раскручена.",
                 "Где мне найти соавтора для книги?",
                 "Кругом одни предатели, никому нельзя довериться!",
                 "Вы на сервер придете когда-нибудь, сычи?",
                 "Слушай меня, дурень: you suck.",
                 "Это просто недопустимо! ****!",
                 "Deploy the nukes! *спрятался в бункере*",
                 "С читерами не разговариваю.",
                 "У меня еще есть шансы попасть в серебро!",
                 "Завистники!",
                 "*достал дробан* Живо прекращай эту упоротость!",
                 "*упражняется во владении посохом вращая его вокруг себя и перебирая из рук в руки*",
                 "JUST DO IT YOURSELF DAMN IT!",
                 "О Боже. Теперь о религии заговорили.",
                 "*радуется, что родился не во времена СССР*",
                 "Такие вещи не принято обсуждать, чтобы моральный дух не упал.",
                 "Порой вы такие странные, что ужас дикий.",
                 "Вы вообще люди или просто кучка гиен?"]

def reply(bot, update):
    a = random.randint(0,3)
    #update.message.reply_text(str(a))
    if a == 0:
        update.message.reply_text(Levap_replica[random.randint(0,len(Levap_replica))])

updater = Updater('829807051:AAGwMUS5eAvJ15xKIOwMdbmbGr_MUosg7Wo')

updater.dispatcher.add_handler(MessageHandler(Filters.all, reply))

updater.start_polling()
updater.idle()
