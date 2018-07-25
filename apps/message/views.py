# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import UserMessage
import re
# Create your views here.

def getform(request):
    # return render(request,'message_form.html')

    #UserMessage默认的数据管理器是objects
    #方法all()将所有数据返回成一个queryset类型

    full_path = request.get_full_path()
    r = re.search('\?(\w)=(\d{4})&(\w)=(\d{4})&(\w{2})=(\d)&(\w)=(\d)&(\w{2})=(\d{7})',full_path).groups()
    sn = ''
    for i in r:
        sn += i
    sn = sn.upper()
    print(sn)
    message = UserMessage.objects.get(serial_num=sn)
    return render(request,'message_form.html',{'my_message': message})