from django.urls import path,include
from . import views
urlpatterns = [
    path('listings',views.home,name='listings'),
    path('<int:listin_id>/',views.listing,name='listing'),
    path('search',views.search,name='search'),
]
