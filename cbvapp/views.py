from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView
from cbvapp.models import Company,Product

# Create your views here.
# class Classname(View):
#     def get(self, request):
#         return HttpResponse("<h1>This is Class Baesd View. </h1>")

class Myclass(TemplateView):
    template_name="index.html"

class AllCompanies(ListView):
    model=Company

class CompanieDetails(DetailView):
    model=Company
    context_object_name="mycompanies"

class AddNewCompany(CreateView):
    model=Company
    fields='__all__'

