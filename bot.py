from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from serpapi import GoogleSearch
import os
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
def start(Update,context):
    Update.message.reply_text("What do you want to see")
def text(Update,context):
    query=Update.message.text
    theurl="https://www.google.com/search?q="+query+"&source=lnms&tbm=isch"
    r = requests.get(theurl)
    print(r)
    soup = BeautifulSoup(r.text, "lxml")
    print(soup)
    link = soup.find("img", {"class":"yWs4tf","src":True})['src']
    Update.message.reply(query)
    Update.message.reply_photo(link)
TOKEN="1619203815:AAFVMcnbJ_dk5W4a0XlEN6s1grx0pDrv8xI"
updater=Updater(TOKEN,use_context=True)
dispatcher=updater.dispatcher
dispatcher.add_handler(CommandHandler("start",start))
dispatcher.add_handler(MessageHandler(Filters.text,text))
updater.start_polling()
updater.idle()





