from django.urls import path
from django.views.generic.base import RedirectView
from .views import (TweetListApiView, TweetCreateApiView)
app_name = 'api-tweet'

urlpatterns = [
    path('', TweetListApiView.as_view(), name='list'),
    path('create/', TweetCreateApiView.as_view(), name='create')

]
