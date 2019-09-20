#!/usr/bin/env python3
from telegram.ext import Updater
from telegram.ext import CommandHandler
import telegram
from redditcrawler import get_hot_threads
from reddithelpers import Thread
import credentials


def start(update, context):
    text = f"Olá! Sou o bot do Bruno!\n\nPara receber uma lista das threads "\
           f"\"bombantes\" (upvotes >= 5000) de SubReddits, utilize o comand"\
           f"o /nadaparafazer [SubReddit1];[SubReddit2].\n\nComo usar:\n/nad"\
           f"aparafazer cats;lego\n/nadaparafazer cats lego"
    update.message.reply_html(text)


def nadaparafazer(update, context):
    context.bot.send_chat_action(chat_id=update.effective_message.chat_id,
                                 action=telegram.ChatAction.TYPING)

    # if user sent nadaparafazer command with no arguments, return usage msg
    if len(context.args) == 0:
        text = f"Você precisa passar uma lista de SubReddits para o comando"\
               f"/nadaparafazer.\nPode ser usando ; ou espaço para separá-l"\
               f"os.\n\nExemplos:\n/nadaparafazer cats;lego\n/nadaparafazer"\
               f" cats lego"
        update.message.reply_text(text, parse_mode=telegram.ParseMode.HTML)

    # if only one argument is received, try to split using the ';' separator
    if len(context.args) == 1:
        context.args = context.args[0].split(';')
    subreddits = context.args

    # get hot threads
    hot_threads = get_hot_threads(subreddits)

    # return message (if found hot threads or not)
    if len(hot_threads):
        update.message.reply_text(f"<b>Threads que estão bombando:</b>",
                                  parse_mode=telegram.ParseMode.HTML)
        for index, thread in enumerate(hot_threads):
            text = f"<b>{index+1}</b>: {thread.title}\nSubReddit: "\
                   f"{thread.subreddit}\nUpvotes: {thread.up_votes}\nLink: "\
                   f"<a href=\"{thread.link}\">{thread.link}</a>\n\n<a href"\
                   f"=\"{thread.comments_link}\">Link para os comentários"\
                   f"</a>\n\n"
            update.message.reply_html(text)
    else:
        update.message.reply_html('Não encontrei nenhuma thread bombando. 😔')


def teste(update, context):
    update.message.reply_text("Teste")


# Create Telegram Bot Updater and Dispatcher
updater = Updater(token=credentials.TELEGRAM_API_KEY, use_context=True)
dispatcher = updater.dispatcher

# Create handler to reply to "/start" command
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Create handler to reply to "/nadaparafazer" command
nadaparafazer_handler = CommandHandler('nadaparafazer',
                                       nadaparafazer,
                                       pass_args=True)
dispatcher.add_handler(nadaparafazer_handler)

# Create handler to reply to "/teste" command
teste_handler = CommandHandler('teste', teste)
dispatcher.add_handler(teste_handler)

# Start checking for messages
updater.start_polling()

