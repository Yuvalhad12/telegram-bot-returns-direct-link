import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from fetch_link import get_info
import re
regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)



ACCESS_TOKEN = ''

def fetch_link(url):
    ydl_opts ={'simulate': 'true'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
        if 'pornhub' in url:
            return info['url']

        else:
            return 'not supported yet'





def reply_with_link(update, context):
    if not re.match(regex, update.message.text):
        update.message.reply_text('not a link. try again')
    else:
        update.message.reply_text(get_info(update.message.text))


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(ACCESS_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher



    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_with_link))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
