from typing import List
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
# Create your views here.
from .models import Topic,PolicyConditions
from django.views.generic import TemplateView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import SubTopicDetailForm
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.db.models import Count



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
        context['policyconditions'] = PolicyConditions.objects.get(pk=1)    
        context['last_read'] = Topic.objects.filter(read_by=self.request.user).last()     

        user_topics_read = Topic.objects.filter(read_by=self.request.user)
        num_topics_read = user_topics_read.count()
        total_topics = Topic.objects.all().count()
        percentage = round((num_topics_read / total_topics) * 100)
        context['percentage'] = percentage
        context['total_topics'] = total_topics
        context['num_topics_read'] = num_topics_read
        
        return context



class TopicReadToggleView(LoginRequiredMixin, UpdateView):
    model = Topic
    fields = []
    template_name = 'lessons/topicsimple.html'

    def post(self, request, *args, **kwargs):
        topic = self.get_object()
        if request.user in topic.read_by.all():
            topic.read_by.remove(request.user)
        else:
            topic.read_by.add(request.user)
        topic.save()
        # return redirect('topic_detail', topic.id)
        return redirect('home')
