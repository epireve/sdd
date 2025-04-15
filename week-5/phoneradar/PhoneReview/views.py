from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Brand, PhoneModel, Review

# Create your views here.

def brand_list(request):
    brands = Brand.objects.all().order_by('name')
    return render(request, 'PhoneReview/brand_list.html', {'brands': brands})

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    phones = brand.models.all().order_by('-launch_date')
    return render(request, 'PhoneReview/brand_detail.html', {
        'brand': brand,
        'phones': phones
    })

def phone_list(request):
    phones = PhoneModel.objects.all().order_by('-launch_date')
    return render(request, 'PhoneReview/phone_list.html', {'phones': phones})

def phone_detail(request, phone_id):
    phone = get_object_or_404(PhoneModel, pk=phone_id)
    reviews = phone.reviews.all().order_by('-date_published')
    return render(request, 'PhoneReview/phone_detail.html', {
        'phone': phone,
        'reviews': reviews
    })

def review_list(request):
    reviews = Review.objects.all().order_by('-date_published')
    return render(request, 'PhoneReview/review_list.html', {'reviews': reviews})

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'PhoneReview/review_detail.html', {'review': review})

def index(request):
    context = {'title': 'Welcome to PhoneReview!'}
    return render(request, template_name='PhoneReview/index.html', context=context)

@login_required
def add_review(request):
    # This is just a placeholder view for now
    # In a real implementation, this would include form handling
    return render(request, 'PhoneReview/add_review.html') 