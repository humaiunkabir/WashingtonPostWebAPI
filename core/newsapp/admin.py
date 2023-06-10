from django.contrib import admin
from newsapp.models import NewsPost
# Register your models here.

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display=('id','title','content','images')