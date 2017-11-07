from django.db import models
from django.contrib.auth.models import AbstractUser

class ZUser(AbstractUser):
    qq=models.IntegerField(u'qq',blank=True,unique=True)
    mobile=models.IntegerField(u'手机号',blank=True,unique=True)
    login_status=models.BooleanField(u'是否锁定',default=False)
    is_login=models.BooleanField(u'是否登录',default=False)
    info=models.TextField(u'个人介绍',blank=True,null=True)
    work=models.CharField(u'公司',blank=True,null=True,max_length=60)
    zhiwei=models.CharField(u'职位',blank=True,null=True,max_length=60)
    home=models.CharField(u'居住地',max_length=25,blank=True,null=True)
    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name
        ordering=['-id']
    def __str__(self) :
        return self.username
from huati.models import Hua
class Shoucang(models.Model):
    user=models.ForeignKey(ZUser)
    name=models.CharField(u'收藏夹名字',max_length=255)
    hua=models.ManyToManyField(Hua)
    status=models.BooleanField(u'状态',default=False)
    class Meta:
        verbose_name = u'收藏夹名字'
        verbose_name_plural = verbose_name
        ordering = ['-id']
    def __str__(self):
        return self.name
class Message(models.Model):
    user_id=models.ForeignKey(ZUser)
    messages=models.TextField(u'私信内容')
    send_date=models.DateTimeField(u'发送时间',auto_now_add=True)
    is_read=models.BooleanField(u'是否读',default=False)
    status = models.BooleanField(u'状态', default=False)
    resce_user=models.CharField(u'收信人',max_length=255)
    class Meta:
        verbose_name = u'私信'
        verbose_name_plural = verbose_name
        ordering = ['-id']
    def __str__(self):
        return self.messages
class Guanzhu(models.Model):
    user=models.ForeignKey(ZUser)
    guanzhu=models.ManyToManyField(Hua)
    add_time=models.DateTimeField(u'关注时间',auto_now_add=True)
    class Meta:
        verbose_name = u'关注'
        verbose_name_plural = verbose_name
        ordering = ['-id']
    def __str__(self):
        return self.guanzhu
class Caogao(models.Model):
    user=models.ForeignKey(ZUser)
    neirong = models.ManyToManyField(Hua)
    status=models.BooleanField(u'状态',default=False)
    class Meta:
        verbose_name = u'草稿'
        verbose_name_plural = verbose_name
        ordering = ['-id']
    def __str__(self):
        return self.neirong






