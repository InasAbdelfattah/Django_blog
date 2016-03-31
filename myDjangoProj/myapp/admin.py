from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(User)
admin.site.register(User_role)
admin.site.register(Article)
admin.site.register(View)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Emotion)
admin.site.register(System_status)
