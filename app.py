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

from __future__ import unicode_literals, absolute_import

import unittest

from linebot.models import (
    TemplateSendMessage,
    CarouselTemplate,
    CarouselColumn,
    ImageCarouselTemplate,
    ImageCarouselColumn,
    ConfirmTemplate,
    ButtonsTemplate,
    PostbackAction,
    URIAction,
    MessageAction,
)

from tests.models.serialize_test_case import SerializeTestCase


class TestTemplate(SerializeTestCase):
    def test_template(self):
        arg = {
            'type': 'template',
            'alt_text': 'This is a buttons template',
            'template':
                ButtonsTemplate(
                    thumbnail_image_url='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
                    image_aspect_ratio='rectangle',
                    image_size='cover',
                    image_background_color='#FFFFFF',
                    title='Menu',
                    text='Please select',
                    default_action=URIAction(label='View detail',
                                             uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
                    actions=[
                        PostbackAction(label='Buy', data='action=buy&itemid=155'),
                        URIAction(label='View detail', uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
                    ]
                )
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.TEMPLATE),
            TemplateSendMessage(**arg).as_json_dict()
        )

    def test_button_template(self):
        arg = {
            'type': 'buttons',
            'thumbnail_image_url': 'https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
            'image_aspect_ratio': 'rectangle',
            'image_size': 'cover',
            'image_background_color': '#FFFFFF',
            'title': 'Menu',
            'text': 'Please select',
            'default_action': URIAction(label='View detail',
                                        uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
            'actions': [
                PostbackAction(label='Buy', data='action=buy&itemid=155'),
                URIAction(label='View detail', uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.BUTTONS),
            ButtonsTemplate(**arg).as_json_dict()
        )

    def test_confirm_template(self):
        arg = {
            'type': 'confirm',
            'text': 'Are you sure?',
            'actions': [
                MessageAction(label='Yes', text='yes...'),
                MessageAction(label='No', text='no...'),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.CONFIRM),
            ConfirmTemplate(**arg).as_json_dict()
        )

    def test_carousel_template(self):
        arg = {
            'image_aspect_ratio': 'rectangle',
            'image_size': 'cover',
            'columns': [
                CarouselColumn(
                    thumbnail_image_url='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
                    image_background_color='#FFFFFF',
                    title='this is menu',
                    text='description',
                    default_action=URIAction(label='View detail',
                                             uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
                    actions=[
                        PostbackAction(label='Buy', data='action=buy&itemid=155'),
                        URIAction(label='View detail', uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
                    image_background_color='#000000',
                    title='this is menu',
                    text='description',
                    default_action=URIAction(label='View detail',
                                             uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
                    actions=[
                        PostbackAction(label='Buy', data='action=buy&itemid=555'),
                        URIAction(label='View detail', uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
                    ]
                )
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.CAROUSEL),
            CarouselTemplate(**arg).as_json_dict()
        )

    def test_carousel_column(self):
        arg = {
            'thumbnail_image_url': 'https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
            'image_background_color': '#FFFFFF',
            'title': 'this is menu',
            'text': 'description',
            'default_action': URIAction(label='View detail',
                                        uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
            'actions': [
                PostbackAction(label='Buy', data='action=buy&itemid=155'),
                URIAction(label='View detail', uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            CarouselColumn(**arg).as_json_dict()
        )

    def test_image_carousel_template(self):
        arg = {
            'columns': [
                ImageCarouselColumn(
                    image_url='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
                    action=PostbackAction(label='Buy', data='action=buy&itemid=555')
                ),
                ImageCarouselColumn(
                    image_url='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
                    action=MessageAction(label='Yes', text='yes')
                ),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.IMAGE_CAROUSEL),
            ImageCarouselTemplate(**arg).as_json_dict()
        )

    def test_image_carousel_column(self):
        arg = {
            'image_url': 'https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
            'action': PostbackAction(label='Buy', data='action=buy&itemid=555')
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            ImageCarouselColumn(**arg).as_json_dict()
        )

x = TestTemplate()
hasil = TestTemplate.test_template()

if __name__ == '__main__':
    unittest.main()

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from_user = event.message.text
    if msg_from_user == 'Data-covid':
    	message = TextSendMessage(hasil)
    	line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
