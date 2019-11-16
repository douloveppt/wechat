from flask import Flask, request, make_response
from wechatpy import parse_message
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

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
        print(xml)
        msg = parse_message(xml)
        print(msg.content)
        return str(msg)
