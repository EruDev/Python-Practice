from django.db import models


class BookInfoManager(models.Manager):

    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete=False)

    def create(self, btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcomment = 0
        b.isDelete = False

        return b


class BookInfo(models.Model):

    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    books1 = models.Manager()
    books2 = BookInfoManager()

    @classmethod
    def create(cls, btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcomment = 0
        b.isDelete = False

        return b


class HeroInfo(models.Model):

    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey(BookInfo)