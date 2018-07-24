
from django.shortcuts import render

from .models import UserMessage
# Create your views here.

def getform(request,id):
    # return render(request,'message_form.html')

    #UserMessage默认的数据管理器是objects
    #方法all()将所有数据返回成一个queryset类型
    all_message = UserMessage.objects.all()
    for message in all_message:
        print(message.name)
    return render(request,'message_form.html',{'my_message':all_message[id]})