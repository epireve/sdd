from django.urls import path
from . import views

urlpatterns = [
    path('brands/', views.brand_list, name='brand_list'),
    path('brands/<int:brand_id>/', views.brand_detail, name='brand_detail'),
    path('phones/', views.phone_list, name='phone_list'),
    path('phones/<int:phone_id>/', views.phone_detail, name='phone_detail'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/<int:review_id>/', views.review_detail, name='review_detail'),
    path('add-review/', views.add_review, name='add_review'),
] 