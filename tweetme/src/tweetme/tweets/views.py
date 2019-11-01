from django.shortcuts import render
from .models import Tweet
from django.views.generic import (
    DetailView, ListView, CreateView, UpdateView, DeleteView)
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.


class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/tweet_add.html'

    # login_url = '/admin/'


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/tweet_update.html'


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy("tweet:list")


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    def get_queryset(self, *args, **kwargs):
        queryset = Tweet.objects.all()
        # print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains=query) | Q(user__username__icontains=query))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweet:create")
        return context


# def tweet_list_view(request):
#     obj = Tweet.objects.all()
#     print(obj)
#     context = {
#         'object': obj
#     }
#     return render(request, "tweets/list_view.html", context)


# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)
#     print(obj)
#     context = {
#         'object': obj
#     }
#     return render(request, "tweets/detail_view.html", context)
