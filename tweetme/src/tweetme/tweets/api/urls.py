from django.urls import path
from django.views.generic.base import RedirectView
from .views import (TweetListApiView, TweetCreateApiView, RetweetApiView)
app_name = 'api-tweet'

urlpatterns = [
    path('', TweetListApiView.as_view(), name='list'),
    path('create/', TweetCreateApiView.as_view(), name='create'),
    path('<int:pk>/retweet/', RetweetApiView.as_view(), name='retweet'),

]
