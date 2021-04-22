import os
import re
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Header, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage, StickerMessage, \
    StickerSendMessage, FlexSendMessage
from lotify.client import Client
from pydantic import BaseModel

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

router = APIRouter(
    prefix="/webhooks",
    tags=["chatbot"],
    responses={404: {"description": "Not found"}},
)


class Line(BaseModel):
    destination: str
    events: List[Optional[None]]


@router.post("/line")
async def callback(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="chatbot handle body error.")
    return 'OK'


def reserve_location():
    return FlexSendMessage(alt_text='請查看', contents={
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip10.jpg",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "320:213"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "熊大咖啡廳",
                            "weight": "bold",
                            "size": "sm",
                            "wrap": True
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                },
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                },
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                },
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                },
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "4.0",
                                    "size": "xs",
                                    "color": "#8c8c8c",
                                    "margin": "md",
                                    "flex": 0
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "uri",
                                        "label": "預約",
                                        "uri": "https://spot.line.me/"
                                    }
                                }
                            ]
                        }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                }
            },
            {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip11.jpg",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "320:213"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "兔兔餐廳",
                            "weight": "bold",
                            "size": "sm",
                            "wrap": True
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                },
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                },
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                },
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                },
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "4.0",
                                    "size": "sm",
                                    "color": "#8c8c8c",
                                    "margin": "md",
                                    "flex": 0
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                                "type": "uri",
                                                "label": "預約",
                                                "uri": "https://ezstore.line.me/"
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                }
            },
            {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip12.jpg",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "320:213"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "饅頭人攀岩場",
                            "weight": "bold",
                            "size": "sm"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                },
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                },
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                },
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                                },
                                {
                                    "type": "icon",
                                    "size": "xs",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                                },
                                {
                                    "type": "text",
                                    "text": "4.0",
                                    "size": "sm",
                                    "color": "#8c8c8c",
                                    "margin": "md",
                                    "flex": 0
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                                "type": "uri",
                                                "label": "預約",
                                                "uri": "https://www.linefriends.com.tw/"
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                }
            }
        ]
    })


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    reply_event = TextSendMessage(text=event.message.text)
    if re.search('^優惠卷\s+', event.message.text):
        data = re.sub('^優惠卷\s+', "", event.message.text)
        if data == '12345':
            reply_event = [TextSendMessage(text='您的優惠序號已啟動，請持續關注此頻道'),
                           StickerSendMessage(package_id='6632', sticker_id='11825385'),
                           reserve_location()]
        else:
            rand_text = ['您的優惠碼有誤，請重新輸入', '好了啦 我知道你沒有優惠卷', '就已經發完了啊 我也沒辦法']
            rand_sticker = [StickerSendMessage(package_id='6362', sticker_id='11087938'),
                            StickerSendMessage(package_id='1070', sticker_id='17873'),
                            StickerSendMessage(package_id='6632', sticker_id='11825393')]
            import random
            rand = random.randint(0, len(rand_text) - 1)
            reply_event = [TextSendMessage(rand_text[rand]), rand_sticker[rand]]
    line_bot_api.reply_message(
        event.reply_token,
        reply_event
    )


@handler.add(MessageEvent, message=StickerMessage)
def sticker_text(event):
    if ('brown' in event.message.keywords or 'edward' in event.message.keywords) \
            and os.getenv('LOTIFY_SWITCH') == 'ON':

        user = line_bot_api.get_profile(user_id=event.source.user_id)
        lotify = Client()
        lotify.send_message(
            access_token=os.getenv('LOTIFY_TOKEN'),
            message=f'🎉 {user.display_name} 🏃‍♂️ {user.picture_url}')
        sticker = StickerSendMessage(package_id='6136', sticker_id='10551379')
    else:
        sticker = StickerSendMessage(package_id='8525', sticker_id='16581310')
    line_bot_api.reply_message(
        event.reply_token,
        sticker
    )
