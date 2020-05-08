from django.shortcuts import render
from studentsapp.models import student
from django.http import HttpResponse

import logging
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from datetime import datetime
from flask import Flask
from flask import request
from flask import abort
from linebot.models import *
logger = logging.getLogger("django")

"""
line_bot_api = LineBotApi(settings.CHANNEL_ACCESS_TOKEN)
parser  = WebhookParser(settings.LINE_CHANNEL_SECRET)

"""
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('528gEzSdPX8Pw9mTJlfpXRpTBdETmaT0LJuHs8+3/qBsiz1lWzBRIfWXQexgOdiPyGxeLtL9HAggCjAp0LBJcqKAdv7h8Ux5JQpKMioyobyYoBQpwer/eA3cA1e89/b80sl219M34lvpXlAAFud++wdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('43664ae683e1af5eb58087c85b74216d')

line_bot_api.push_message('Ub8e3cf75739079f25a50f82b2cbd4c63', TextSendMessage(text='你可以開始了'))

@csrf_exempt
@require_POST
def callback(request):
    signature = request.META['HTTP_X_Line_Signature']
    body = request.body.decode('utf-8')

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        messages = ( "Invalid signature. Please check your channel access token/channel secret.")
        HttpResponseForbidden()

    return HttpResponse('OK',status=200)


@handler.add(event=MessageEvent, message=TextMessage)
def handl_message(event: MessageEvent):
           line_bot_api.reply_message(
            reply_token=event.reply_token,
            messages=TextSendMessage(text=event.message.text),
        )
	
def index1(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def sayhello (request):
  return HttpResponse("hello django!/")

def hello2 (request,username):
  return HttpResponse("hello "+ username)

def hello3 (request,username):
          
                now=datetime.now()
                return render(request,"hello3.html",locals())

def index(request):
                now=datetime.now()
                username="daphne lo" 
                return render(request,"Resume.html",locals())

def listone(request): 
	try: 
		unit = student.objects.get(cName="李采茜") #讀取一筆資料
	except:
  		errormessage = " (讀取錯誤!)"
	return render(request, "listone.html", locals())

def listall(request):  
	students = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
	return render(request, "listall.html", locals())
	
def insert(request):  #新增資料
    cName = '邱心怡'
    cSex =  'M'
    cBirthday =  '1987-12-26'
    cEmail = 'bear@superstar.com'
    cPhone =  '0963245612'
    cAddr =  '台北市信義路18號'
    unit = student.objects.create(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail,cPhone=cPhone, cAddr=cAddr) 
    unit.save()  #寫入資料庫
    students = student.objects.all().order_by('-id')  #讀取資料表, 依 id 遞減排序
    return render(request, "listall.html", locals())
	
def modify(request):  #刪除資料
    unit = student.objects.get(cName='邱心怡')
    unit.cBirthday =  '1986-12-11'
    unit.cAddr = '台北市信義路234號'
    unit.save()  #寫入資料庫
    students = student.objects.all().order_by('-id')
    return render(request, "listall.html", locals())
	
def delete(request,id=None):  #刪除資料
    unit = student.objects.get(cName='邱心怡')
    unit.delete()
    students = student.objects.all().order_by('-id')
    return render(request, "listall.html", locals())
