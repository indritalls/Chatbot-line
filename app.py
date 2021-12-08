import random
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, StickerMessage, StickerSendMessage
)

app = Flask(__name__)

ACCESS_TOKEN = 'lIKFwU/TgvvYQAVMTT0V3L/Q4MJUnjZFb4TdtVb4xeb3YRAVMkRusqyAiIifWjdhFzwiWPT0u8F4B9iB1ILEjXqWEjNEy9xvClCqk8xnFjPVfl1MLFsJ/k6nam1Y94ksJNiLuuU0poOvR905pXJ8JwdB04t89/1O/w1cDnyilFU='
SECRET = 'f470cac6f78984857d780a3b2a5e90fd'

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from_user = event.message.text
    if msg_from_user == 'Bisa':
        line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id='11537',
            sticker_id='52002735'))

        message = TextSendMessage('Ingin lanjut? Jika lanjut, ketik "truth" untuk memilih games truth dan ketik "dare" untuk memilih games dare.')
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
