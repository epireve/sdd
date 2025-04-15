from django.contrib import admin
from django.urls import path
from .views import GameReviewListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("reviews/", GameReviewListView.as_view(), name="review-list"),
]
