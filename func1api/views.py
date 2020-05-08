from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
#from linebot.models import MessageEvent, TextSendMessage
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent
from module import func
from urllib.parse import parse_qsl
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '@傳送文字':
                        func.sendText(event)
    
                    elif mtext == '@傳送圖片':
                        func.sendImage(event)
                    elif mtext == '@傳送聲音':
                        func.sendVoice(event)
    
                    elif mtext == '@傳送影片':
                        func.sendVedio(event)
                    elif mtext == '@傳送貼圖':
                        func.sendStick(event)
    
                    elif mtext == '@多項傳送':
                        func.sendMulti(event)
    
                    elif mtext == '@傳送位置':
                        func.sendPosition(event)
    
                    elif mtext == '@快速選單':
                        func.sendQuickreply(event)
              
                    elif mtext == '@按鈕樣板':
                        func.sendButton(event)
    
                    elif mtext == '@確認樣板':
                        func.sendConfirm(event)
    
                    elif mtext == '@轉盤樣板':
                        func.sendCarousel(event)
    
                    elif mtext == '@圖片轉盤':
                        func.sendImgCarousel(event)
    
                    elif mtext == '@購買披薩':
                        func.sendPizza(event)
    
                    elif mtext == '@yes':
                        func.sendYes(event)
                    elif mtext == '@圖片地圖':
                        func.sendImgmap(event)
                    elif mtext == '@日期時間':
                        func.sendDatetime(event)
                    elif mtext == '@彈性配置':
                        func.sendFlex(event)
                    elif mtext[:3] == '###' and len(mtext) > 3:
                         func.manageForm(event, mtext)    

    
            if isinstance(event, PostbackEvent):  #PostbackTemplateAction觸發此事件
                backdata = dict(parse_qsl(event.postback.data))  #取得data資料
                if backdata.get('action') == 'sell':
                    func.sendData_sell(event, backdata)

            else:            
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
    
        return HttpResponse()

    else:
        return HttpResponseBadRequest()
