from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import permission_required
from views import EntryListView, LatestEntriesFeed, EntryCreate, EntryUpdate
from django.views.generic import DetailView
from models import Entry
import api

urlpatterns = patterns('blogalog.views', 
    url(r'^$', EntryListView.as_view(
            queryset=api.list_visible_entries().order_by('-pub_date'),
            context_object_name='latest_blog_entries',
        ), 
        name='entry-list'
    ),
    url(r'^feed/?$', LatestEntriesFeed()),
    url(r'^entry/(?P<pk>\d+)/?$', DetailView.as_view(
            queryset=api.list_visible_entries(),
            context_object_name='entry',
        ), 
        name='entry-detail',
    ),
    url(r'^entry/add/?$', permission_required('blogalog.add_entry')(EntryCreate.as_view()), name='entry-add'),
    url(r'^entry/update/(?P<pk>\d+)/?$', permission_required('blogalog.change_entry')(EntryUpdate.as_view()), name='entry-update'),
)
