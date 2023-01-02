from typing import List
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
from .models import Topic
from django.views.generic import TemplateView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import SubTopicDetailForm
from django.http import HttpResponse, HttpResponseRedirect


class AllTopicsSimple(ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'lessons/topicsimple.html'
    paginate_by = 10
    queryset = Topic.objects.all()
    # slug_field = 'slug'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['topics'] = Topic.objects.all()      
        return context

