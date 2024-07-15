from django.urls import path
from . import views 
from .views import * 

urlpatterns = [

    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', ContactView.as_view(), name = 'contact'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('team/', views.team, name = 'team'),
    path('pricing/', views.pricing, name = 'pricing'),
    path('shoppingwindow/', views.shop, name = 'product'),
    path('services/', views.services, name = 'services'),
    
]

