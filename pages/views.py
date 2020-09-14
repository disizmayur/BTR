from django.shortcuts import render
from Listings.models import listing
from realtors.models import Realtor
from Listings.choice import state_choice,price_choice,bedroom_chice 
# Create your views here.
def home(request):
    listings=listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings':listings,
        'state_choice':state_choice,
        'bedroom_choice':bedroom_chice,
        'price_choice':price_choice
    }
    return render(request, 'pages/home.html',context)

def about(request):
    realtor=Realtor.objects.order_by('-hire_date')
    mvp_realtor=Realtor.objects.all().filter(is_mvp=True)
    context={
        'realtor':realtor,
        'mvp_realtor':mvp_realtor
    }
    return render(request,'pages/about.html',context)