"""DjangoGetStarted URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,register_converter,re_path
from apps.message import views

# class UrlParamsConverter:
#     regex = 'form\?w=\d{4}&t=\d{4}&ms=\d&g=\d&np=\d{7}'
#
#     def to_python(self,value):
#         return int(value)
#
#     def to_url(self,value):
#         return '%04d' % value
#
# register_converter(UrlParamsConverter,)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/',views.getform)
    # re_path(r'form/(?P<w>[0-9]{4})',views.getform)
    #form\?w=(?P<w>\d{4})&t=(?P<t>\d{4})&ms=(?P<ms>\d)&g=(?P<g>\d)&np=(?P<np>\d{7})

]
