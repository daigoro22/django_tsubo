from typing import List
from django.shortcuts import render
from django.views.generic import(
    ListView,
    DetailView,
)
from .models import BlogModel

# Create your views here.
class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel
