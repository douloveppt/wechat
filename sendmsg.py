from wechatpy import WeChatClient

from constant import AppID, AppSecret, OpenId

client = WeChatClient(appid=AppID, secret=AppSecret)


def send_msg(content):
    response = client.message.send_text(OpenId, content)
    return response
