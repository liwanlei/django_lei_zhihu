from django.db import models
from  coustmer.models import ZUser
class Huafen(models.Model):
    id = models.AutoField(primary_key=True)
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
    wenzhang='文章'
    tiwen='提问'
    new_fen = (
        (wenzhang, u'文章'),
        (tiwen, u'提问')
    )
    id=models.AutoField(primary_key=True)
    title=models.CharField(u'标题',max_length=255)
    desc=models.CharField(u'简述',max_length=255,blank=True,null=True)
    connet=models.TextField(u'话题内容')
    time=models.DateTimeField(u'发表时间',auto_now_add=True)
    user=models.ForeignKey(ZUser)
    fenlei=models.ManyToManyField(Huafen,related_name='fenlei',null=True,blank=True)
    is_shi=models.BooleanField(u'是否匿名',default=False)
    status = models.BooleanField(u'是否冻结', default=False)
    guanzhu_num=models.IntegerField(u'关注人数',default=0)
    liu_num=models.IntegerField(u'浏览人数',default=0)
    yaoqing=models.CharField(u'邀请人',max_length=255,blank=True,null=True)
    leibie = models.CharField(max_length=4, choices=new_fen,default=wenzhang)
    class Meta:
        verbose_name = u'话题'
        verbose_name_plural = verbose_name
        ordering=['-time']
    def __str__(self) :
        return self.title
    def getfenlei(self):
        fenlei_list=[]
        for fenlei in self.fenlei.all():
            fenlei_list.append(fenlei)
        return  fenlei_list
    def save(self, *args, **kwargs):
        if not self.id:
            super(Hua, self).save(*args, **kwargs)
        super(Hua, self).save(*args, **kwargs)
class Commenthuati(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(ZUser)
    huati=models.ForeignKey(Hua,blank=True,null=True)
    time=models.DateTimeField(u'话题评论时间',auto_now_add=True)
    comment=models.TextField(u'话题评论内容')
    dianzan=models.IntegerField(u'点赞',default=0)
    status=models.BooleanField(u'是否冻结',default=False)
    pid=models.ForeignKey('self',blank=True,null=True)
    class Meta:
        verbose_name = u'话题评论'
        verbose_name_plural = verbose_name
        ordering=['-time']
    def __str__(self) :
        return self.comment
