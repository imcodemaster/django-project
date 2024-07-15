from django.contrib import admin
from .models import Contact , Product 
from django.contrib.admin.options import ModelAdmin
# Register your models here.
class ContactAdmin(ModelAdmin):
	list_display = ['first_name','second_name', 'email', 'mobile' , 'message', 'date']
	search_field = ['first_name','second_name', 'mobile', 'email']
	list_filter = [ 'first_name','second_name', 'mobile' , 'email' , 'date']

admin.site.register(Contact, ContactAdmin)

admin.site.register(Product)
