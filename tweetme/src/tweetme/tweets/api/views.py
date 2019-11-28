from django.contrib.auth.models import User
from .serializers import TweetModelSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from tweets.models import Tweet
from django.db.models import Q
from rest_framework import permissions
from .pagination import StandardResultPagination


class TweetCreateApiView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TweetListApiView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultPagination

    def get_queryset(self):
        im_following = self.request.user.profile.get_following()
        qs1 = Tweet.objects.filter(
            user__in=im_following)
        qs2 = Tweet.objects.filter(
            user=self.request.user)
        queryset = (qs1 | qs2).distinct().order_by("-timestamp")
        query = self.request.GET.get("q", None)
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains=query) | Q(
                    user__username__icontains=query)
            )
        return queryset
