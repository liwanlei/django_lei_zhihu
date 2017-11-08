from django.db import models
from  coustmer.models import ZUser
class Huafen(models.Model):
    name=models.CharField(u'话题分类',max_length=32)
    user=models.ForeignKey(ZUser)
    time=models.DateTimeField(u'创建时间',auto_now_add=True)
    status=models.BooleanField(u'是否冻结',default=False)
    class Meta:
        verbose_name = u'话题分类'
        verbose_name_plural = verbose_name
        ordering = ['-time']
    def __str__(self):
        return self.name
class Hua(models.Model):
    new_fen = (
        (0, u'提问'),
        (1, u'话题')
    )
    title=models.CharField(u'标题',max_length=255)
    connet=models.TextField(u'话题内容')
    time=models.DateTimeField(u'发表时间',auto_now_add=True)
    user=models.ForeignKey(ZUser)
    fenlei=models.ManyToManyField(Huafen)
    is_shi=models.BooleanField(u'是否匿名',default=False)
    status = models.BooleanField(u'是否冻结', default=False)
    guanzhu_num=models.IntegerField(u'关注人数',default=0)
    liu_num=models.IntegerField(u'浏览人数',default=0)
    yaoqing=models.CharField(u'邀请人',max_length=255)
    leibie = models.CharField(max_length=4, choices=new_fen)
    class Meta:
        verbose_name = u'话题'
        verbose_name_plural = verbose_name
        ordering=['-time']
    def __str__(self) :
        return self.title

class Commenthuati(models.Model):
    user=models.ForeignKey(ZUser)
    time=models.DateTimeField(u'话题评论时间',auto_now_add=True)
    comment=models.TextField(u'话题评论内容')
    dianzan=models.IntegerField(u'点赞',default=0)
    status=models.BooleanField(u'是否冻结',default=False)
    pid=models.ForeignKey('self')
    class Meta:
        verbose_name = u'话题评论'
        verbose_name_plural = verbose_name
        ordering=['-time']
    def __str__(self) :
        return self.comment
