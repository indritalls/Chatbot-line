from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, FlexSendMessage, 
    TemplateSendMessage, ConfirmTemplate, PostbackTemplateAction, MessageTemplateAction,
    ButtonsTemplate, URITemplateAction
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
    if msg_from_user == 'Tes':
        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.pinimg.com/564x/0d/b8/98/0db89880dfa0595585f33ddb50da89f9.jpg',
                title='Menu',
                text='Please select',
                actions=[
                    URITemplateAction(
                        label='uri',
                        uri='https://indritall.wordpress.com/'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
