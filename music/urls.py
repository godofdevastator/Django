from django.conf.urls import url
from .import views

app_name = "music"

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumDelete.as_view(), name='album-delete'),
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),

]