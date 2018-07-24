from django.contrib import admin
from .models import UserMessage
# Register your models here.

class UserMessageAdmin(admin.ModelAdmin):
    # fields = ['object_id','name','email','address','message']
    fields = ['serial_num','install_date','installer','test_date','tester','changed_device','changed_device_time'
              ,'errs','holder','destination']

admin.site.register(UserMessage,UserMessageAdmin)