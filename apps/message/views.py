# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import UserMessage
# Create your views here.

def getform(request):
    # return render(request,'message_form.html')

    #UserMessage默认的数据管理器是objects
    #方法all()将所有数据返回成一个queryset类型

    params = request.GET.dict()
    #拼接关键字参数,获得serail_num
    sn = ''
    for k,v in params.items():
        sn += k.upper()+v
    print('sn',sn,type(sn))
    print('items:',params.items())
    message = UserMessage.objects.get(serial_num=sn)
    return render(request,'message_form.html',{'my_message': message})