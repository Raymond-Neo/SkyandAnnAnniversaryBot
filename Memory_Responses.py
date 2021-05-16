import requests
import telegram
from telegram import *
import API_KEY_CONSTANT
from telegram.ext import *
year_one_bool = False
year_two_bool = False
year_three_bool = False
def yearone_Response(update,context):
    # set inline keyboard buttons
    global year_one_bool
    if year_one_bool == False:
        update.effective_message.reply_text("remember the time when I am still in the last year of Poly, and we use to "
                                        + "always travel to school everyday on the shuttle bus and then meeting at the "
                                        + "library after class so we can head back together😁 It was also the year I "
                                        + "graduation from Ngee Ann and enlisted into national service, a significant "
                                        + "year where 3 major milestone happened, Ns, Graduation and you  , remember "
                                        +"the times when i used devotion to get close and spend time with you😁😘 there "
                                        + "are some photos and videos below how you enjoy 😎")
    keyboard = [
        [InlineKeyboardButton("Year 1: 1st Half", callback_data='1.1')],
        [InlineKeyboardButton("Year 1: 2nd Half", callback_data='1.2')],
        [InlineKeyboardButton("Return to Year", callback_data='return')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.effective_message.reply_text("Please select a Half", reply_markup=reply_markup)

def yeartwo_Response(update,context):
    # set inline keyboard buttons
    global year_two_bool
    if year_two_bool == False:
        update.effective_message.reply_text("This year is the year where covid strikes the world, many different in "
                                            + "The "
                                        +"way of life, when we have got lesser opportunities to meet, initially due to "
                                        +"NS , then covid made it worse. With the isolations and circuit breakers it "
                                        +"really broke our cycle and many of out usually practices. Remember how we "
                                        +"use to always call every single day and how we use to meet almost every "
                                        +"single day to the extend that we felt that it may even become a problem 🤪 "
                                        +"but again I believe its covid that allowed us reconstruct for the better, "
                                        +"it unintentionally help us solve our worries and I believe till today it "
                                        +"have only help is to grow and be more mature and better! Weell with that "
                                        +"said we still have many memories forged this year! Hahaha watch watch as "
                                        +"we reminisce through the wonderful memories 🤩")
    keyboard = [
        [InlineKeyboardButton("Year 2: 1st Half", callback_data='2.1')],
        [InlineKeyboardButton("Year 2: 2nd Half", callback_data='2.2')],
        [InlineKeyboardButton("Return to Year", callback_data='return')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.effective_message.reply_text("Please select a Half", reply_markup=reply_markup)

def yearthree_Response(update,context):
    # set inline keyboard buttons
    global year_three_bool
    if year_three_bool == False:
        update.effective_message.reply_text("This is the year we made many decisions, a year that I believe God have "
                                        + "shown you many different miracles, a year that God have put in place to "
                                        + "help you grow both physically and spiritually 🥳 It was also a special year "
                                        + "for you where you had your graduation. A year which is very fast pace, and "
                                        + "many changes were made in church too, from the new renovations to the wall "
                                        + "painting, new cameras, new roles and positions, new friendships. Its a "
                                        + "wonderful year despite the present of Covid. It is also a significant year "
                                        + "as I ORD in end July! Its been a long journey, and I got to say, God have "
                                        + "preserved me and our relationship in the time of my service. Many stories, "
                                        + "many examples, many experiences, but God have watch over me and you, and I "
                                        + "must say I am thankful for this year! And enjoy the memories from this "
                                        + "wonderful year!")
    keyboard = [
        [InlineKeyboardButton("Year 3: 1st Half", callback_data='3.1')],
        [InlineKeyboardButton("Year 3: 2nd Half", callback_data='3.2')],
        [InlineKeyboardButton("Return to Year", callback_data='return')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.effective_message.reply_text("Please select a Half", reply_markup=reply_markup)

def yearone_FirstHalf(update, context):
    global year_one_bool
    year_one_bool = True
    #open file for year 1 first half
    photo1 = {'photo': open(r'Photos\Year1\FirstHalf\1.jpeg', 'rb')}
    photo2 = {'photo': open(r'Photos\Year1\FirstHalf\2.jpeg', 'rb')}
    photo3 = {'photo': open(r'Photos\Year1\FirstHalf\3.jpeg', 'rb')}
    photo4 = {'photo': open(r'Photos\Year1\FirstHalf\4.jpeg', 'rb')}
    photo5 = {'photo': open(r'Photos\Year1\FirstHalf\5.jpeg', 'rb')}
    photo6 = {'photo': open(r'Photos\Year1\FirstHalf\6.jpeg', 'rb')}
    photo7 = {'photo': open(r'Photos\Year1\FirstHalf\7.jpeg', 'rb')}
    photo8 = {'photo': open(r'Photos\Year1\FirstHalf\8.jpeg', 'rb')}
    photo9 = {'photo': open(r'Photos\Year1\FirstHalf\9.jpeg', 'rb')}
    photo10 = {'photo': open(r'Photos\Year1\FirstHalf\10.jpeg', 'rb')}

    #instantiate self
    bot = telegram.Bot('1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo')

    #get current chat
    chat_id = update.effective_message.chat.id
    print(chat_id)

    #post image to chat
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
    'sendPhoto?chat_id=' + f"{chat_id}", files=photo1)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo2)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo3)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo4)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo5)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo6)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo7)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo8)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo9)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo10)


    #send video to chat
    '''
    bot.sendVideo(chat_id=f"{chat_id}",
    video=open(r'C:/Users/rayra/PycharmProjects/LTanniversary/Videos/Sample.mp4', 'rb'),
    supports_streaming=True)
    '''
    yearone_Response(update, context)

def yearone_SecondHalf(update, context):
        global year_one_bool
        year_one_bool = True

        # open file for year 1 second half
        photo1 = {'photo': open(r'Photos\Year1\SecondHalf\1.jpeg', 'rb')}
        photo2 = {'photo': open(r'Photos\Year1\SecondHalf\2.jpeg', 'rb')}
        photo3 = {'photo': open(r'Photos\Year1\SecondHalf\3.jpeg', 'rb')}
        photo4 = {'photo': open(r'Photos\Year1\SecondHalf\4.jpeg', 'rb')}
        photo5 = {'photo': open(r'Photos\Year1\SecondHalf\5.jpeg', 'rb')}
        photo6 = {'photo': open(r'Photos\Year1\SecondHalf\6.jpeg', 'rb')}
        photo7 = {'photo': open(r'Photos\Year1\SecondHalf\7.jpeg', 'rb')}
        photo8 = {'photo': open(r'Photos\Year1\SecondHalf\8.jpeg', 'rb')}
        photo9 = {'photo': open(r'Photos\Year1\SecondHalf\9.jpeg', 'rb')}
        photo10 = {'photo': open(r'Photos\Year1\SecondHalf\10.jpeg', 'rb')}

        # instantiate self
        bot = telegram.Bot('1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo')

        # get current chat
        chat_id = update.effective_message.chat.id
        print(chat_id)

        # post image to chat
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo1)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo2)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo3)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo4)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo5)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo6)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo7)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo8)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo9)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo10)

        # send video to chat
        '''
        bot.sendVideo(chat_id=f"{chat_id}",
        video=open(r'C:/Users/rayra/PycharmProjects/LTanniversary/Videos/Sample.mp4', 'rb'),
        supports_streaming=True)
        '''
        yearone_Response(update, context)

def yeartwo_FirstHalf(update, context):
    global year_two_bool
    year_two_bool = True
    #open file for year 2 first half
    photo1 = {'photo': open(r'Photos\Year2\FirstHalf\1.jpeg', 'rb')}
    photo2 = {'photo': open(r'Photos\Year2\FirstHalf\2.jpeg', 'rb')}
    photo3 = {'photo': open(r'Photos\Year2\FirstHalf\3.jpeg', 'rb')}
    photo4 = {'photo': open(r'Photos\Year2\FirstHalf\4.jpeg', 'rb')}
    photo5 = {'photo': open(r'Photos\Year2\FirstHalf\5.jpeg', 'rb')}
    photo6 = {'photo': open(r'Photos\Year2\FirstHalf\6.jpeg', 'rb')}
    photo7 = {'photo': open(r'Photos\Year2\FirstHalf\7.jpeg', 'rb')}
    photo8 = {'photo': open(r'Photos\Year2\FirstHalf\8.jpeg', 'rb')}

    #instantiate self
    bot = telegram.Bot('1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo')

    #get current chat
    chat_id = update.effective_message.chat.id
    print(chat_id)

    #post image to chat
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
    'sendPhoto?chat_id=' + f"{chat_id}", files=photo1)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo2)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo3)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo4)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo5)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo6)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo7)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo8)


    # send video to chat
    '''
    bot.sendVideo(chat_id=f"{chat_id}",
    video=open(r'C:/Users/rayra/PycharmProjects/LTanniversary/Videos/Sample.mp4', 'rb'),
    supports_streaming=True)
    '''
    yeartwo_Response(update, context)

def yeartwo_SecondHalf(update, context):
        global year_two_bool
        year_two_bool = True
        # open file for year 2 second half
        photo1 = {'photo': open(r'Photos\Year2\SecondHalf\1.jpeg', 'rb')}
        photo2 = {'photo': open(r'Photos\Year2\SecondHalf\2.jpeg', 'rb')}
        photo3 = {'photo': open(r'Photos\Year2\SecondHalf\3.jpeg', 'rb')}
        photo4 = {'photo': open(r'Photos\Year2\SecondHalf\4.jpeg', 'rb')}
        photo5 = {'photo': open(r'Photos\Year2\SecondHalf\5.jpeg', 'rb')}
        photo6 = {'photo': open(r'Photos\Year2\SecondHalf\6.jpeg', 'rb')}
        photo7 = {'photo': open(r'Photos\Year2\SecondHalf\7.jpeg', 'rb')}

        # instantiate self
        bot = telegram.Bot('1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo')

        # get current chat
        chat_id = update.effective_message.chat.id
        print(chat_id)

        # post image to chat
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo1)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo2)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo3)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo4)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo5)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo6)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo7)


        # send video to chat
        bot.sendVideo(chat_id=f"{chat_id}",
                      video=open(r'C:\Users\rayra\PycharmProjects\LTanniversary\Photos\Year2\SecondHalf\8.mp4', 'rb'),
                      supports_streaming=True)

        yeartwo_Response(update, context)

def yearthree_FirstHalf(update, context):
    global year_three_bool
    year_three_bool = True
    #open file for year 3 first half
    photo1 = {'photo': open(r'Photos\Year3\FirstHalf\1.jpeg', 'rb')}
    photo2 = {'photo': open(r'Photos\Year3\FirstHalf\2.jpeg', 'rb')}
    photo3 = {'photo': open(r'Photos\Year3\FirstHalf\3.jpeg', 'rb')}
    photo4 = {'photo': open(r'Photos\Year3\FirstHalf\4.jpeg', 'rb')}
    photo5 = {'photo': open(r'Photos\Year3\FirstHalf\5.jpeg', 'rb')}
    photo6 = {'photo': open(r'Photos\Year3\FirstHalf\6.jpeg', 'rb')}

    #instantiate self
    bot = telegram.Bot('1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo')

    #get current chat
    chat_id = update.effective_message.chat.id
    print(chat_id)

    #post image to chat
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
    'sendPhoto?chat_id=' + f"{chat_id}", files=photo1)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo2)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo3)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo4)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo5)
    requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                  'sendPhoto?chat_id=' + f"{chat_id}", files=photo6)


    # send video to chat
    '''
    bot.sendVideo(chat_id=f"{chat_id}",
    video=open(r'C:/Users/rayra/PycharmProjects/LTanniversary/Videos/Sample.mp4', 'rb'),
    supports_streaming=True)
    '''

    yearthree_Response(update, context)

def yearthree_SecondHalf(update, context):
        global year_three_bool
        year_three_bool = True
        # open file for year 3 second half
        photo1 = {'photo': open(r'Photos\Year3\SecondHalf\1.jpeg', 'rb')}
        photo2 = {'photo': open(r'Photos\Year3\SecondHalf\2.jpeg', 'rb')}
        photo3 = {'photo': open(r'Photos\Year3\SecondHalf\3.jpeg', 'rb')}
        photo4 = {'photo': open(r'Photos\Year3\SecondHalf\4.jpeg', 'rb')}
        photo5 = {'photo': open(r'Photos\Year3\SecondHalf\5.jpeg', 'rb')}
        photo6 = {'photo': open(r'Photos\Year3\SecondHalf\6.jpeg', 'rb')}

        # instantiate self
        bot = telegram.Bot('1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo')

        # get current chat
        chat_id = update.effective_message.chat.id
        print(chat_id)

        # post image to chat
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo1)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo2)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo3)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo4)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo5)
        requests.post('https://api.telegram.org/bot1712123477:AAEVFUInHP9V7eYkedBqieNpUu4acp9cMYo/' +
                      'sendPhoto?chat_id=' + f"{chat_id}", files=photo6)


        # send video to chat
        '''
        bot.sendVideo(chat_id=f"{chat_id}",
        video=open(r'C:/Users/rayra/PycharmProjects/LTanniversary/Videos/Sample.mp4', 'rb'),
        supports_streaming=True)
        '''

        yearthree_Response(update, context)