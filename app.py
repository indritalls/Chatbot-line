import random
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage
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
    t = {'https://i.pinimg.com/564x/c9/04/87/c904872af76b3e8013fb614c6f5d6853.jpg':1, 
        'https://i.pinimg.com/564x/70/ce/46/70ce46df1f2d280c79bf4fd59dc5f9ac.jpg':2,
        'https://i.pinimg.com/564x/85/24/99/8524995c523e066019646fc7d88b994f.jpg' :3,
        'https://i.pinimg.com/564x/23/21/e0/2321e08e70e0ffd054c6453f1fb6f076.jpg':4,
        'https://i.pinimg.com/564x/cc/e1/3a/cce13a149ebe97d6b8883fbcd20cb054.jpg':5,
        }
    tth = random.choice(list(t.keys()))
    msg_from_user = event.message.text
    if msg_from_user == 'Data-covid':
        line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url='https://1.bp.blogspot.com/-eaDZ7sDP9uY/Xhwqlve5SUI/AAAAAAABXBo/EcI2C2vim7w2WV6EYy3ap0QLirX7RPohgCNcBGAsYHQ/s400/pose_syanikamaeru_man.png',
            preview_image_url='https://i.pinimg.com/564x/70/cf/b5/70cfb5748a1986676a9f623b4cc6cc70.jpg'))
    if msg_from_user == 'Hukuman':
        line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url='https://i.pinimg.com/236x/88/a8/ee/88a8eec5497b774af25910cd23b3f2ea.jpg',
            preview_image_url=tth))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
