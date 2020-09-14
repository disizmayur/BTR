from django.shortcuts import render,redirect
from .models import contacts
# Create your views here.
def contacts(request):
    if request.method=="POST":
        listings=request.POST['listings']
        listings_id=request.POST['listings_id']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']

        contact=contacts(listings=listings,listings_id=listings_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()
        return redirect('/listings/'+listings_id)