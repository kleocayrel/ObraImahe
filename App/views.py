from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'App/home.html'

class AboutPage(TemplateView):
    template_name = 'App/about.html'