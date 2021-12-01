import operator
import random

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

score = 0
opslist = {operator.add: "+", operator.sub: "-", operator.mul: "x"} #All operators that can be chosen
num1,num2 = random.randint(1,10), random.randint(1,10)        #Two Random Numbers          
ops = random.choice(list(opslist.keys()))        # random operators from oplist keys                        
ActualAnswer = (ops(num1,num2))                #Answer for my quiz                                

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from_user = event.message.text
    if msg_from_user == 'Kuis':
            message = TextSendMessage(num1,opslist[ops],num2)
    	    line_bot_api.reply_message(event.reply_token, message)
             
            userAns = (int(input("Enter answer:")))
            if userAns == ActualAnswer:        
                message = TextSendMessage("benar")
    	        line_bot_api.reply_message(event.reply_token, message)
                return 1
            else:
                message = TextSendMessage("salah")
    	        line_bot_api.reply_message(event.reply_token, message)
                nilai = score - 0
            return 0
    
    totalScore = 0
    for i in range (10):
        totalScore += handle_message()

    message = TextSendMessage("Kuis telah selesai")
    line_bot_api.reply_message(event.reply_token, message)

    message = TextSendMessage("Today you achieved a score of" ,totalScore,"out of 10")
    line_bot_api.reply_message(event.reply_token, message)  

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

