import telebot
import telegram
from telegram import *
import API_KEY_CONSTANT
from telegram.ext import *
import Responses as r
import Memory_Responses
import requests

def start_command(update, context):
    update.effective_message.reply_text("Hello baby\n"
                                        + "Note: Always /start to return to top\n"
                                        + "Please enter /joke for a random joke\n"
                                        + "Please enter /guide for bot functions(only do this when you have experienced"
                                        + " the whole bot)\n"
                                        + "or enter hello to continue")

def help_command(update, context):
    update.message.reply_text("If you need help you should ask for help on Google")

def joke_command(update,context):
    r.get_joke(True)
    update.effective_message.reply_text(f'Here is the joke:\"{r.joke_setup}\"\n{r.joke_punchline}')

def guide_command(update, context):
    update.message.reply_text("/start to start bot opening \n"
                             + "/help when you really need help \n"
                             + "/joke when you need a cold laugh\n"
                             + "/memories when you feel like looking back\n"
                            + "/dog for some dog video compilation I just found\n"
                            + "/credit if you want a fabulous picture of the creator")

def dog_command(update, context):
    bot = telegram.Bot('1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo')
    bot.send_message(chat_id=update.message.chat_id,
                     text="<a href='https://www.youtube.com/watch?v=1HygThMLzGs'>Dog Video</a>",
                     parse_mode=ParseMode.HTML)

def memory_command(update, context):

    #set inline keyboard buttons
    keyboard = [
        [InlineKeyboardButton("Year 1", callback_data='1')],
        [InlineKeyboardButton("Year 2", callback_data='2')],
        [InlineKeyboardButton("Year 3", callback_data='3')],
        [InlineKeyboardButton("Exit", callback_data='0')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.effective_message.reply_text("Please select a year to start with.", reply_markup=reply_markup)

def credit_command(update, context):
    chat_id = update.effective_message.chat.id
    update.effective_message.reply_text("@rayray_neo")
    photo1 = {'photo': open(r'Photos\Creator.jpg', 'rb')}
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo1)

def button(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    #query.edit_message_text(text=f"Selected option: {query.data}")

    if query.data == '1':
        query.edit_message_text('Year chosen: 1')
        Memory_Responses.yearone_Response(update, context)
    elif query.data == '1.1':
        Memory_Responses.yearone_FirstHalf(update, context)
    elif query.data == '1.2':
        Memory_Responses.yearone_SecondHalf(update, context)

    elif query.data == '2':
        query.edit_message_text('Year chosen: 2')
        Memory_Responses.yeartwo_Response(update, context)
    elif query.data == '2.1':
        Memory_Responses.yeartwo_FirstHalf(update, context)
    elif query.data == '2.2':
        Memory_Responses.yeartwo_SecondHalf(update, context)

    elif query.data == '3':
        query.edit_message_text('Year chosen: 3')
        Memory_Responses.yearthree_Response(update, context)
    elif query.data == '3.1':
        Memory_Responses.yearthree_FirstHalf(update, context)

    elif query.data == '3.2':
        Memory_Responses.yearthree_SecondHalf(update, context)


    elif query.data == 'return':
        memory_command(update, context)
        Memory_Responses.year_one_bool = False
        Memory_Responses.year_two_bool = False
        Memory_Responses.year_three_bool = False
    else:
        query.edit_message_text('Menu Exited')
        start_command(update, context)


def handle_message(update, CallbackContext):
    text = str(update.message.text).lower()
    response = r.conversation_responses(text)

    update.message.reply_text(response)


def error_message(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(API_KEY_CONSTANT.API_KEY, use_context=True)
    dp = updater.dispatcher
    # for /start
    dp.add_handler(CommandHandler("start", start_command))
    # for /help
    dp.add_handler(CommandHandler("help", help_command))
    # for /memories
    dp.add_handler(CommandHandler("memories", memory_command))
    #for /guide
    dp.add_handler(CommandHandler("guide", guide_command))
    # for /joke
    dp.add_handler(CommandHandler("joke", joke_command))
    # for /dog
    dp.add_handler(CommandHandler("dog", dog_command))
    # for /credit
    dp.add_handler(CommandHandler("credit", credit_command))
    #for buttons
    dp.add_handler(CallbackQueryHandler(button))
    # Handle incoming messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error_message)

    updater.start_polling()
    updater.idle()


main()




