from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import requests
import json

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
    pesan = event.message.text
    if pesan == 'data':
        message = TextSendMessage("ayam")
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
