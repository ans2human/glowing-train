from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProfileList.as_view(), name='profile-list'),
    url(r'add/timeline/$', views.manage_articles, name='w-list'),
    url(r'timeline/$', views.timeline_view, name='timeline_view'),
    url(r'profile/add/$', views.ProfileFamilyMemberCreate.as_view(), name='profile-add'),
    url(r'profile/(?P<pk>[0-9]+)/$', views.ProfileFamilyMemberUpdate.as_view(), name='profile-update'),
    url(r'profile/(?P<pk>[0-9]+)/delete/$', views.ProfileDelete.as_view(), name='profile-delete'),
]
