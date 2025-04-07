from django.contrib import admin
from .models import Brand, PhoneModel, Review

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin', 'manufacturing_since')
    search_fields = ('name', 'origin')
    list_filter = ('origin',)

@admin.register(PhoneModel)
class PhoneModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'brand', 'launch_date', 'platform')
    list_filter = ('brand', 'platform', 'launch_date')
    search_fields = ('model_name', 'brand__name', 'platform')
    date_hierarchy = 'launch_date'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published', 'rating')
    list_filter = ('author', 'date_published')
    search_fields = ('title', 'content', 'author')
    date_hierarchy = 'date_published'
    filter_horizontal = ('models',)
