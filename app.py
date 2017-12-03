# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('iUOqb7vvlRsoKP4DK0Y97+ncmnB1fCAkbc4+L+qpxMRLpUG0AnKc4uFI/m3NYflMprGxNu/UYZvwjXC5ZIVHA/9IfQSEL/90AEL9ls7PlOVff+RtkkQ2pL/1bhOrDZo7/4jhVaCn1XugMh9280whkQdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('b21a656c004d2dd1f7eb202ca9bbf7e5') #Your Channel Secret

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

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
