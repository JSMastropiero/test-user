from django.contrib import admin
from .models import Article, Comment, File, TypeOfFile, Profile

# Register your models here.


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(File)
admin.site.register(TypeOfFile)
admin.site.register(Profile)
