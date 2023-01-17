"""Alteernlingual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin


from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from alteernlingual_user import views
import alteernlingual_user
from django.contrib.auth import views as auth_views
from Alteernlingual_topic.views import TopicReadToggleView
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    # path('', AllTopicsSimple.as_view(), name='home'),
     path('topic/<int:pk>/read/', TopicReadToggleView.as_view(), name='topic_read_toggle'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),


    # path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    # path('accounts/signup/', views.register_request, name='signup'),
    # path('accounts/logout/', views.logout_request, name='logout'),
    path('', include('alteernlingual_user.urls')),
    path('', include('Alteernlingual_topic.urls')),
    # path('subjects/', include('alteernlingual_subjects.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('i18n/', include('django.conf.urls.i18n')),

    
  

    #social auth
    # path('social-auth/', include('social_django.urls', namespace="social")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)