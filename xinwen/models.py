from django.db import models
from coustmer.models import Use
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
    title=models.CharField(u'新闻标题',max_length=50)
    desc=models.CharField(u'新闻描述',max_length=50)
    content=models.TextField(u'新闻内容')
    click_count=models.IntegerField(u'点击次数',default=0)
    date_publish=models.DateTimeField(u'发布时间',auto_now_add=True)
    is_recommend=models.BooleanField(u'是否推荐',default=False)
    users=models.ForeignKey(Use)
    objects=NewManager()
    class Meta:
        verbose_name = u'新闻'
        verbose_name_plural = verbose_name
        ordering=['-date_publish']
    def __str__(self) :
        return self.title
