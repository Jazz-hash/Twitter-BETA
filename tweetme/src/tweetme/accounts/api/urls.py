from django.urls import path
from tweets.api.views import (TweetListApiView)

app_name = 'tweet'
urlpatterns = [
    path('<slug:username>/tweet/', TweetListApiView.as_view(), name='list'),
]
