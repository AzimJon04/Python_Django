from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'Home.html'

class AboutSite(TemplateView):
    template_name = 'About.html'

class ProductsPage(TemplateView):
    template_name = 'Products.html'

class AdsPages(TemplateView):
    template_name = 'Ads.html'