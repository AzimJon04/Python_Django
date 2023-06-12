from django.urls import path
from .views import HomePageView, AboutSite, ProductsPage, AdsPages

urlpatterns = [
    path('', HomePageView.as_view(), name='Home'),
    path('about/', AboutSite.as_view(), name='About'),
    path('products/', ProductsPage.as_view(), name='Products'),
    path('ads/', AdsPages.as_view(), name='Ads')
]