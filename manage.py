from flask import Flask, request, make_response
from wechatpy import parse_message
from wechatpy.replies import TextReply
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

from sendmsg import send_msg

app = Flask(__name__)

_TOKEN = 'wangbibo'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        signature = request.args.get("signature", "")
        timestamp = request.args.get("timestamp", "")
        nonce = request.args.get("nonce", "")
        echostr = request.args.get("echostr", "")
        try:
            check_signature(_TOKEN, signature, timestamp, nonce)
            return echostr
        except InvalidSignatureException as e:
            raise e
    if request.method == 'POST':
        xml = request.data
        msg = parse_message(xml)
        if msg.type == 'text':
            # content = msg.content
            # response = send_msg(content)
            # print(response)
            reply = TextReply(content='你好', message=msg)
            reply_xml = reply.render()
            return reply_xml
        elif msg.type == 'image':
            reply = TextReply(content='sorry, 我目前还看不懂图片哦~', message=msg).render()
            return reply
        elif msg.type == 'voice':
            reply = TextReply(content='你说了个啥？？？', message=msg).render()
            return reply
        elif msg.type == 'link':
            reply = TextReply(content='这啥？', message=msg).render()
            return reply
        else:
            reply = TextReply(content='不懂', message=msg).render()
            return reply
