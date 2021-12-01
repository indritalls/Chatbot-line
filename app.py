import sys
from random import randint

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
#tambahkan ini#########################
import requests
import json
url = "https://api.kawalcorona.com/indonesia/"
response = requests.get(url)
parsed = response.json()[0]
negara = parsed["name"]
positif = parsed["positif"]
sembuh = parsed["sembuh"]
meninggal = parsed["meninggal"]

count = 0
 
Soal = ["Social Media buatan Mark zuck...? ","Social Media yang eksis dengan awake sleep? ","Microblogging yang gambar burung apa hayo? ","Social Media yang populer dengan photo?","Social Media yang logonya hampir sama dengan Path  ", "Social Media buat pekerja itu namanya: ", "Planet Python di Indonesia itu hanya: "]
Jawab = ["facebook","path", "twitter", "instagram", "pinterest", "linkedin", "planpin"]
########################################
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('GUw/Sdi+cGaiCtLq8ZdrYaOMTLk4K1Tc6R0DRiEH/vBqQljRKQ3pJq+oN1sYKNSeSqIPRMJS/H1sBEBIJuxLat77L1VtPgRBnssLOC48ICWaIEk1f9oixGL+aeqgL7mEe6hjk7HUwjSAqjdLBeQA0gdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('923c01d65919b7ae347b0749bde3bb6d')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from_user = event.message.text
    if msg_from_user == 'Data-covid':
    	message = TextSendMessage("Data COVID-19 " + negara + "\nPositif: " + positif + "\nSembuh: " + sembuh + "\nMeninggal: " + meninggal)
    	line_bot_api.reply_message(event.reply_token, message)
        
    count = 0
    msg_from_user = event.message.text
    if msg_from_user == 'Data-covid':
    	message = TextSendMessage("Data COVID-19 " + negara + "\nPositif: " + positif + "\nSembuh: " + sembuh + "\nMeninggal: " + meninggal)
    	line_bot_api.reply_message(event.reply_token, message)
    
    i = randint(0, 7)
    answer = input("Pertanyaan 1 : " + Soal[i])
    if answer.lower() == Jawab[i]: 
        count = count + 1
        message = TextSendMessage("benar"+"\nKamu benar"+count)
    	line_bot_api.reply_message(event.reply_token, message)  
    else:
        message = TextSendMessage("salah")
    	line_bot_api.reply_message(event.reply_token, message)

    i = randint(0, 7) 
    answer = input("\nPertanyaan 2 : " + Soal[i])
    if answer.lower() == Jawab[i]:
        count = count + 1
        message = TextSendMessage("benar"+"\nKamu benar"+count)
    	line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage("salah")
    	line_bot_api.reply_message(event.reply_token, message)
