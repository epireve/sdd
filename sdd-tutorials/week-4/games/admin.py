from django.contrib import admin
from .models import Game, Tags, Review


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("label",)
    search_fields = ("label",)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "developer", "platform")
    list_filter = ("platform", "label_tag")
    search_fields = ("title", "developer")
    filter_horizontal = ("label_tag",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("game", "date")
    list_filter = ("date", "game")
    search_fields = ("review", "game__title")
    date_hierarchy = "date"
