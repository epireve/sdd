from django.shortcuts import render
from django.http import HttpResponse
from PhoneReview.models import Brand, PhoneModel, Review

# Create your views here.
def index(request):
    # Get latest reviews, featured brands and phones
    latest_reviews = Review.objects.order_by('-date_published')[:3]
    featured_brands = Brand.objects.all()[:5]
    latest_phones = PhoneModel.objects.order_by('-launch_date')[:6]
    
    context = {
        'latest_reviews': latest_reviews,
        'featured_brands': featured_brands,
        'latest_phones': latest_phones,
    }
    
    return render(request, 'main/index.html', context)
