from django.contrib import admin
from .models import Game, Review, Tags

# Register your models here.
admin.site.register(Game)
admin.site.register(Review)
admin.site.register(Tags)
