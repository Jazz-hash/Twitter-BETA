from django.urls import path
from .views import (UserDetailView, UserFollowView)
from django.views.generic.base import RedirectView

app_name = 'profiles'
urlpatterns = [
    # path('', RedirectView.as_view(url="/"), name='home'),
    # path('search/', TweetListView.as_view(), name='list'),
    path('<slug:username>', UserDetailView.as_view(), name='detail'),
    path('<slug:username>/follow/', UserFollowView.as_view(), name='follow'),
    # path('create/', TweetCreateView.as_view(), name='create'),
    # path('<int:pk>/update', TweetUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete', TweetDeleteView.as_view(), name='delete'),

]
