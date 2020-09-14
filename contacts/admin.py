from django.contrib import admin
from .models import contacts
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display=('id','name','listing','email','phone','contact_date')
    list_dispaly_link=('id','name')
    search_fields=('name','email','listing')
    list_per_page=25

admin.site.register(contacts,contactAdmin)