from django.urls import path
from django.views.generic.base import RedirectView
from .views import (TweetListApiView, TweetCreateApiView,
                    RetweetApiView, LikeToggleApiView)
app_name = 'api-tweet'

urlpatterns = [
    path('', TweetListApiView.as_view(), name='list'),
    path('create/', TweetCreateApiView.as_view(), name='create'),
    path('<int:pk>/like/', LikeToggleApiView.as_view(), name='like-toggle'),
    path('<int:pk>/retweet/', RetweetApiView.as_view(), name='retweet'),

]
