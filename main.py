import os
import telebot

bot = telebot. TeleBot ("1947857384:AAHSCGN39-e7syB34pezap-gP5TVDgm086w")

@bot.message_handler("commands=["start"])
def send welcome(message):
    bot.reply_to(message,"Hello i'm Hasiya Chat Bot")

@bot.message_handler(commands=["how"])
def send_message(message):
    bot.send_message(message,"https://google.com")

@bot.message_handler(commands=["hasiya"])
def send_message(message:)
    bot.send_message(message,"♻️ COVID 19 UPDATES BOT ♻️ - @Covid_19_Updates_SL_Bot

ᴘʜᴏᴛᴏ ᴇᴅɪᴛᴏʀ ʟᴋ - @Photo_Editor_LK_Bot

ᴛᴇᴄʜ ᴡɪᴅᴇ ʙᴏᴛ ᴘᴏᴡᴇʀᴅ ʙʏ ʜᴀsɪʏᴀ - @Hasiya_Tech_Bot

HASIYA MUSIC - @Music_Downloder_By_Hasiya_Bot

All Bots Made By - @HASIYA_GEEK
😉 Made BY Hasiya 😉")
    bot.polling()
    


    
    
