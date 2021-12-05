from django.urls import path, re_path
from lopez import views
#from .feed import BulletinFeed
from .views import RESTBulletinList, RESTBulletinDetail



urlpatterns = [
    path('datetime/', views.current_datetime),
   # path('', views.bulletin_list),
   # re_path(r'^(?P<bulletin_id>[0-9]+/$', views.bulletin_detail),
    #path('rss/', BulletinFeed(), name='bulletin_rss'),
    path('rest-api/', RESTBulletinList.as_view(), name='rest_bulletin'),
    re_path(r'^rest-api/(?P<pk>[0-9]+)/$', RESTBulletinDetail.as_view(),
    re_path(r'^(?P<id>\d+)/', views.viral_video_detail))]
    #path('register/', views.register))
    