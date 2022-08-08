import os,sys,json,pprint
from flask import Flask, request, abort
from linebot import (
    LineBotApi,  WebhookHandler,  WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

#flask
app = Flask(__name__)

#鍵の定義
channel_secret=os.environ["CHANNEL_SECRET"]
channel_access_token=os.environ["CHANNEL_ACCESS_TOKEN"]

#LINEbot関係のインスタンス
line_bot_api = LineBotApi(channel_access_token)
# handler = WebhookHandler(channel_secret)
parser = WebhookParser(channel_secret)

#example.com/callbackをwebhook URLに設定してる場合
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        print(body)
        # handler.handle = (body, signature)
        events = parser.parse(body, signature)
        event = events[0]
        print(event.message.type)
        if event.message.type == "text":
            print(event.message.text)
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='テキストを受け取りました.')
        )
    except InvalidSignatureError:
        abort(400)

    

    return 'OK'


@app.route('/')
def check():
    return "check1"

# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     msg="「"+event.message.text+"」を受け取りました。"
#     print(msg)
#     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))

#このファイルがインポートされたものでなければ実行する
if __name__=="__main__":
    app.run(port=int(os.getenv("PORT")),host="0.0.0.0")