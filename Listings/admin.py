from django.contrib import admin
from .models import listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published','price','list_date','realtor')
    list_display_links=('id','title')
    list_editable=('is_published',)
    search_fields  =('title','price','city','address','zipcode')

admin.site.register(listing,ListingAdmin)