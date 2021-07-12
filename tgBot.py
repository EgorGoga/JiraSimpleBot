import telebot

import ass_dix

import pandas as pd

bot = telebot.TeleBot('1835667520:AAFgDOku2RJE-ZdTYzYquvR9yaMViFaUMzo')


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Greetings! I can show the tasks in specified sprint.'
    )


@bot.message_handler(commands=['sprint'])
def get_assign(message):
    spr_name = message.text[8:]
    sprint_data = ass_dix.jira_hist(spr_name)
    sprint_assignees = ass_dix.right_version(sprint_data)
    df = pd.DataFrame.from_dict(sprint_assignees, orient='index')
    df.to_excel("df_Sprint.xlsx")
    with open("df_Sprint.xlsx", 'rb') as file:
        bot.send_document(
            message.chat.id,
            file
        )


bot.polling(none_stop=True)
