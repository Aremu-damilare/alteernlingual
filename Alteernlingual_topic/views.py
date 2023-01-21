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
from django.db.models import Q
from django.contrib.auth import logout



class AllTopicsSimple(ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'lessons/topicsimple.html'
    paginate_by = 10
    queryset = Topic.objects.all()
    # title = 'Alteernlingual - Use your language to learn new language'
    # description = 'A technology platform where you can use your preferred language to learn new language,'
    # keywords = ' Yoruba, igbo, Hausa, learn, new language, audio'
    # slug_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(Q(main_explanations__icontains=search_query) | Q(title__icontains=search_query))
        return queryset
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books                

        if self.request.user.is_authenticated:
            user_topics_read = Topic.objects.filter(read_by=self.request.user)
            num_topics_read = user_topics_read.count()
            total_topics = Topic.objects.all().count()
            percentage = round((num_topics_read / total_topics) * 100)
            context['policyconditions'] = PolicyConditions.objects.get(pk=1)    
            context['last_read'] = Topic.objects.filter(read_by=self.request.user).last()
            context['percentage'] = percentage
            context['total_topics'] = total_topics
            context['num_topics_read'] = num_topics_read
        else:
            context['policyconditions'] = PolicyConditions.objects.get(pk=1)    
            context['last_read'] = "Topic.objects.filter(read_by=self.request.user).last()"
            context['percentage'] ="percentage"
            context['total_topics'] = "total_topics"
            context['num_topics_read'] = "num_topics_read"

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
        return redirect('home')



from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Topic

@login_required
def mark_topic_as_read(request, topic_id):
    if request.method == 'POST' and request.is_ajax():
        topic = Topic.objects.get(id=topic_id)
        user = request.user
        
        if request.user in topic.read_by.all():
            topic.read_by.remove(request.user)
        else:
            topic.read_by.add(request.user)

        topic.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


def PrivacyPolicy(request):        
    privacyPolicy = PolicyConditions.objects.get(pk=1)
    context = {
        'privacyPolicy': privacyPolicy,   
    }
    
    return render(request, 'privacy-policy.html', context=context)


def TermsOfService(request):        
    termsOfService = PolicyConditions.objects.get(pk=1)
    
    context = {
        'termsOfService': termsOfService,   
    }
    
    return render(request, 'terms-of-service.html', context=context)    



def logout_view(request):
    logout(request)
    return redirect('home')    