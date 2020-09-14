from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from Listings import models
from django.http import request
from .choice import state_choice,price_choice,bedroom_chice 

# Create your views here.
def home(request):
    listings= models.listing.objects.order_by('-list_date')
    
    return render(request,'Listings/listing.html',{'listings':listings})


def listing(request,listin_id):
    Listing=get_object_or_404(models.listing,pk=listin_id)
    return render(request,'Listings/listings.html',{'Listing':Listing})


def search(request):
    queryset_list=models.listing.objects.order_by('-list_date')

    #keywords
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords) 
        

    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact=city) 

    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            queryset_list=queryset_list.filter(state__iexact=state) 

    if 'bedroom' in request.GET:
        bedroom=request.GET['bedroom']
        if bedroom:
            queryset_list=queryset_list.filter(bedroom__lte=bedroom) 


    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            queryset_list=queryset_list.filter(price__lte=price) 
                       
    context={
        'state_choice':state_choice,
        'bedroom_choice':bedroom_chice,
        'price_choice':price_choice,
        'listings':queryset_list,
        'values':request.GET
    }
    return render(request,'Listings/search.html',context)