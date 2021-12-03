from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('k6Y9+0gsK+ycPoenaZtDwyVeW/hzm8Y8XYmXySGv6yVOkRMhcTgn5H3QjvEY/pnFHpayH9oBeJas4QZa4YswY5UxKR4P4t1vVi955fDVpXej7GL0E2p7F19fHznOQeka/W/m6e5j/2VogY0+d5e2HQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('3c71b07a2d7861abf6a78d8845338baf')

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from_user = event.message.text
    if msg_from_user == 'Data-covid':
    	message = TextSendMessage('Pilih mana?')
    	line_bot_api.reply_message(event.reply_token, message)

    if msg_from_user == 'games':
        message = ImageSendMessage(
            original_content_url='https://d.line-scdn.net/stf/linecorp/ja/pr/design_1.png',
            preview_image_url='https://d.line-scdn.net/stf/linecorp/ja/pr/design_1.png'
        )
        line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
