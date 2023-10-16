from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment']


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ['user', 'podcast']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['tag']
