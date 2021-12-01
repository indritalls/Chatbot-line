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
line_bot_api = LineBotApi('k6Y9+0gsK+ycPoenaZtDwyVeW/hzm8Y8XYmXySGv6yVOkRMhcTgn5H3QjvEY/pnFHpayH9oBeJas4QZa4YswY5UxKR4P4t1vVi955fDVpXej7GL0E2p7F19fHznOQeka/W/m6e5j/2VogY0+d5e2HQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('3c71b07a2d7861abf6a78d8845338baf')

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
        
    if msg_from_user == 'Mulai':
        count = 0
        i = randint(0, 7)
        mmessage = TextSendMessage(input("Pertanyaan 1 : " + Soal[i]))
    	line_bot_api.reply_message(event.reply_token, message)

        if message == Jawab[i]: 
            count = count + 1
            message = TextSendMessage("benar"+"\nKamu benar"+count)
    	    line_bot_api.reply_message(event.reply_token, message)  
        
        else:
            message = TextSendMessage("salah")
    	    line_bot_api.reply_message(event.reply_token, message)
