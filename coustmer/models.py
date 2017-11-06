from django.db import models
from django.contrib.auth.models import AbstractUser
class Use(AbstractUser):
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
