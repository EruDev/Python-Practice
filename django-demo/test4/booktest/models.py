from django.db import models


class BookInfo(models.Model):

    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='bpub_date')
    bread = models.IntegerField()
    bcomment = models.IntegerField()

    class Meta():
        # 定义表名
        db_table = 'booktest_bookinfo'


class HeroInfo(models.Model):

    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField()
    hbook = models.ForeignKey('BookInfo')

    def showname(self):
        return self.hname