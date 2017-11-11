from django.db import models
from django.contrib.auth.models import AbstractUser
class ZUser(AbstractUser):
    id = models.IntegerField(u'id', primary_key=True)
    qq=models.IntegerField(u'qq',blank=True,null=True,unique=True)
    mobile=models.IntegerField(u'手机号',blank=True,null=True,unique=True)
    login_status=models.BooleanField(u'是否锁定',default=False)
    is_login=models.BooleanField(u'是否登录',default=False)
    info=models.TextField(u'个人介绍',blank=True,null=True)
    work=models.CharField(u'公司',blank=True,null=True,max_length=60)
    home=models.CharField(u'居住地',max_length=25,blank=True,null=True)
    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name
        ordering=['-id']
    def __str__(self) :
        return self.username
    def get_follower(self):
        '''
        folloer  关注的人
        :return:
        '''
        user_list = []
        for followed_user in self.followed.all():
            user_list.append(followed_user.follower)
        return user_list
    def get_followed(self):
        '''
        followed 关注我的人
        '''
        user_list = []
        for follower_user in self.follower.all():
            user_list.append(follower_user.followed)
        return user_list
    def get_shoucang(self):
        shoucang_list=[]
        for shoucang in self.shoucanguser.all():
            shoucang_list.append(shoucang.shoucanghua.all())
        return  shoucang_list
from huati.models import Hua
class Shoucang(models.Model):
    shoucanguser=models.ForeignKey(ZUser,related_name='shoucanguser')
    shoucanghua=models.ManyToManyField(Hua,related_name='shoucanghua')
class Message(models.Model):
    id = models.IntegerField(u'id', primary_key=True)
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
    user=models.ForeignKey(ZUser,related_name='guanzhuuser')
    guanzhu=models.ManyToManyField(Hua,related_name='guanzhuhuati')
    add_time=models.DateTimeField(u'关注时间',auto_now_add=True)
class FriendShip(models.Model):
    followed = models.ForeignKey(ZUser,related_name='followed')
    follower = models.ForeignKey(ZUser,related_name='follower')






