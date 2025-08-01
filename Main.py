# TelegramMusic-bot import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '8426776764:AAHrWSisU6xOzDvLTFdmTQ8M4IqbUvGaeA4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_start(message):
    username = message.from_user.
    markup = InlineKeyboardMarkup()

    # Məlumat düymələri
    markup.add(
        InlineKeyboardButton(text="Owner: @Helios_077", url="https://t.me/Helios_077"),
        InlineKeyboardButton(text="Qrup Linki", url="https://t.me/veten_1")
    )
    markup.add(
        InlineKeyboardButton(text="Rəsmi Kanal", url="https://t.me/veten_1")
    )

    bot.send_message(
        message.chat.id,
        f"ᅠ{username} burda start verən admaın adı Salam 👋🏻\n\n"
        "Mənim adım Telegram Music\n"
        "Qrupunuza əlavə etməklə səsli söhbətdə musiqi dinləyə bilərsiniz ✨🎶\n\n"
        "Sora əmrlər üçün aşağıdakı düymələrə klik edə bilərsiniz:",
        reply_markup=markup
    )

# Digər funksiyalar olduğu kimi davam edir
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Əsas əmrlər: /play, /skip, /end, /reload")

@bot.message_handler(commands=['play'])
def handle_play(message):
    query = message.text[6:].strip()
    if not query:
        bot.reply_to(message, "Zəhmət olmasa, mahnı adını qeyd edin.")
        return
    bot.reply_to(message, f"'{query}' oynadır... 🎶\nSorğunuz emal olunur, zəhmət olmasa xətdə qalın...🎧")

@bot.message_handler(commands=['skip'])
def handle_skip(message):
    bot.reply_to(message, "Növbəti mahnıya keçilir... 🎵")

@bot.message_handler(commands=['end'])
def handle_end(message):
    bot.reply_to(message, "Musiqi dayandırıldı və dayandırılır. 🎧")

@bot.message_handler(commands=['reload'])
def handle_reload(message):
    bot.reply_to(message, "Bot yenilənir... 🤖")

@bot.message_handler(func=lambda m: True)
def handle_all(message):
    bot.reply_to(message, "Zəhmət olmasa, əmrlərdən istifadə edin!")

bot.polling()
