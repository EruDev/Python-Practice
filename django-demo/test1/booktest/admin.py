from django.contrib import admin
from .models import BookInfo,HeroInfo


class HeroInfoLine(admin.TabularInline):

    model = HeroInfo
    extra = 3


class BookInfoAdmin(admin.ModelAdmin):

    list_display = ['id', 'btitle', 'bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10
    fields = ['bpub_date', 'btitle']

    inlines = [HeroInfoLine]
    # fieldsets = [
    #     ('base', {'fields': ['btitle']}),
    #     ('super', {'fields': ['bpub_date']})
    # ]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)
