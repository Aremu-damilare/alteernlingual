from django.urls import path, include
from Alteernlingual_topic.views import AllTopicsSimple, PrivacyPolicy, TermsOfService, logout_view, TopicReadToggleView
from django.contrib.sitemaps.views import sitemap


from .sitemaps import LessonListSitemap

sitemaps = {
    'lessons': LessonListSitemap,
}


urlpatterns = [ 	
	path('', AllTopicsSimple.as_view(), name='home'),
    path('privacy-policy', PrivacyPolicy, name='privacypolicy'),
    path('terms-of-service', TermsOfService, name='termsofservice'),
    path('logout', logout_view, name='logout'),
    path('topic/<int:pk>/read/', TopicReadToggleView.as_view(), name='topic_read_toggle'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # # path('topics-simple', views.AllTopicsSimple.as_view(), name='topics_simple'),
    # path('<int:pk>', views.TopicDetail.as_view(), name='detail'),
    # # path('course/<int:pk>', views.subTopicDetail.as_view(), name='topic_detail'),
    # path('follow/<int:pk>', views.followLanguageView.as_view(), name='follow_cat'),
    # path('follow-level/<int:pk>', views.FollowlevelView.as_view(), name='follow_ski'),
    # path('follow-loi/<int:pk>', views.FollowLoiView.as_view(), name='follow_loi'),

    # path('<slug>/read/', views.readView, name='read_topic'),
    # path('search/', views.search, name='search'),

    # path('<int:pk>/add_comment/', views.CommentCreateView, name = 'add_comment'),
]
