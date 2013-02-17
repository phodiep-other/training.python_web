from django.conf.urls import patterns, url
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from entry.models import Entry

urlpatterns = patterns('',
    url(r'^$', 
        ListView.as_view(
            queryset=Entry.objects.order_by('-pub_date')[:5],
            context_object_name='entry',
            template_name="entry/list.html"
        ),
        name="entry_list"),
    url(r'^(?P<pk>\d+)/$', 
        DetailView.as_view(
            model=Entry,
            template_name="entry/detail.html"
        ), name="entry_detail"),
)
