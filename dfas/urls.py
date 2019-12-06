from django.conf.urls import url, include
from . import views

app_name='dfas'
urlpatterns = [
    url(r'^$', views.query_venue_view, name='query_venue_view'),
    url(r'^query_detail_view/(?P<venue_id>[\w-]+)/$', views.query_detail_view, name='query_detail_view'),
    url(r'^query_detail_view/(?P<user_id>[\w-]+)/user_comment_view/$',views.user_comment_view,name='user_comment_view')
]
