from django.db import models

# Create your models here.

class UserMessage(models.Model):
    object_id = models.CharField(max_length=50,primary_key=True,default='',verbose_name='主键')
    name = models.CharField(max_length=20,verbose_name=u'用户名')
    #Django提供内置的邮箱字段会帮忙验证default_validators = [validators.validate_email]
    email = models.EmailField(verbose_name=u'邮箱')
    address = models.CharField(max_length=100,verbose_name=u'联系地址')
    message = models.CharField(max_length=500,verbose_name='留言信息')

    #class Meta，内嵌于 UserMessage 这个类的定义中
    # 如果 class Publisher 是顶格的，那么 class Meta 在它之下要缩进4个空格－－按 Python 的传统
    # 你可以在任意一个 模型 类中使用 Meta 类，来设置一些与特定模型相关的选项。
    # 如：设置ordering = ['name']，默认地都会按 name 字段排序

    class meta:
        verbose_name = u'用户留言信息'
        # db_table = 'user_message'
        # ordering = '-object_id'

        # 指明复数信息，否则后台显示"用户留言s"
        verbose_name_plural = verbose_name