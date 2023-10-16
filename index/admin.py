from django.contrib import admin
from .models import Contact,Subscribe


# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','phone','subject','create']
    list_display_links = ['name','phone']



@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['email']
    list_display_links = ['email']
