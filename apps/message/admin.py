from django.contrib import admin
from .models import UserMessage
# Register your models here.

class UserMessageAdmin(admin.ModelAdmin):
    fields = ['object_id','name','email','address','message']

admin.site.register(UserMessage,UserMessageAdmin)