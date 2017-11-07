from django.db import models
from coustmer.models import ZUser
class Book(models.Model):
    name=models.CharField(u'书名',max_length=255)
    auth=models.CharField(u'作者',max_length=54)
    zishu=models.IntegerField(u'字数',blank=True,null=True)
    sale=models.FloatField(u'售价',blank=True,null=True)
    img=models.URLField(u'图片',blank=True,null=True)
    daoyan=models.TextField(u'导言')
    mulu = models.TextField(u'导言')
    tejia=models.FloatField(u'活动价',null=True,blank=True)
    is_tui=models.BooleanField(u'推荐',default=False)
    add_user=models.ForeignKey(ZUser)
    add_time=models.DateTimeField(u'添加时间',auto_now_add=True)
    status=models.BooleanField(u'状态',default=False)
    class Meta:
        verbose_name = u'书名'
        verbose_name_plural = verbose_name
        ordering = ['-id']
        app_label = 'coustmer'
    def __str__(self):
        return self.name
class  Bookcomment(models.Model):
    book=models.ForeignKey(Book)
    user=models.ForeignKey(ZUser)
    connt=models.TextField(u'内容')
    date=models.DateTimeField(u'评论时间',auto_now_add=True)
    status=models.BooleanField(u'状态',default=False)
    pid=models.ForeignKey('self')
    class Meta:
        verbose_name = u'书的评论'
        verbose_name_plural = verbose_name
        ordering = ['-id']
        app_label = 'coustmer'
    def __str__(self):
        return self.connt
class Bookfenlei(models.Model):
    name=models.CharField(u'分类名',max_length=32)
    adduser=models.ForeignKey(ZUser)
    addtime=models.DateTimeField(u'添加时间',auto_now_add=True)
    sattus=models.BooleanField(u'状态',default=False)
    level=models.IntegerField(u'等级',default=999)
    book=models.ManyToManyField(Book)
    class Meta:
        verbose_name = u'书分类'
        verbose_name_plural = verbose_name
        ordering = ['-id']
        app_label = 'coustmer'
    def __str__(self):
        return self.name




