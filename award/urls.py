from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    url('^$',views.welcome,name = 'welcome'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^edit/profile', views.profile_edit, name='profile_edit'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'project/(\d+)', views.project, name='project'),
    url(r'^comment/(\d+)', views.add_comment, name='comment'),
    url(r'^api/profile/$', views.ProfileList.as_view(),name='profile_list'), 
    url(r'^api/project/$', views.ProjectList.as_view(),name='project_list'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)