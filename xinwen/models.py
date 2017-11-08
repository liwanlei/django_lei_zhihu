from django.db import models
from coustmer.models import ZUser
class NewManager(models.Manager):
    def distinct_date(self):
        distint_daye_lisy=[]
        date_list=self.values('date_publish')
        for date in date_list:
            date=date['date_publish'].strftime('%Y/%m')
            if date not  in distint_daye_lisy:
                distint_daye_lisy.append(date)
        return distint_daye_lisy
class New(models.Model):
    new_fen = (
        (0, u'时政'),
        (1, u'IT'),
        (2, u'国际'),
        (3, u'未分类'),
    )
    title=models.CharField(u'新闻标题',max_length=50)
    desc=models.CharField(u'新闻描述',max_length=50)
    content=models.TextField(u'新闻内容')
    click_count=models.IntegerField(u'点击次数',default=0)
    date_publish=models.DateTimeField(u'发布时间',auto_now_add=True)
    is_recommend=models.BooleanField(u'是否推荐',default=False)
    fenlei=models.CharField(max_length=4,choices=new_fen,default=0)
    status = models.BooleanField(u'是否冻结', default=False)
    users=models.ForeignKey(ZUser)
    objects=NewManager()
    class Meta:
        verbose_name = u'新闻'
        verbose_name_plural = verbose_name
        ordering=['-date_publish']
    def __str__(self) :
        return self.title
class Commentxin(models.Model):
    user=models.ForeignKey(ZUser)
    time=models.DateTimeField(u'评论时间',auto_now_add=True)
    comment=models.TextField(u'评论内容')
    dianzan=models.IntegerField(u'点赞',default=0)
    status=models.BooleanField(u'是否冻结',default=False)
    pid=models.ForeignKey('self')
    class Meta:
        verbose_name = u'新闻评论'
        verbose_name_plural = verbose_name
        ordering=['-time']
    def __str__(self) :
        return self.user
