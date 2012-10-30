from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.sites.models import get_current_site
from django.contrib.syndication.views import Feed
from models import Entry
import api
# Create your views here.

class SiteFilterMixin(object):
    def get_queryset(self):
        #You can append a .filter to this!
        return super(SiteFilterMixin,self).get_queryset()

class EntryListView(SiteFilterMixin, ListView):
    pass

class EntryCreate(CreateView):
    model = Entry

class EntryUpdate(UpdateView):
    model = Entry

class LatestEntriesFeed(Feed):
    title = "Firstyear's blog-a-log"
    link = "/blog/"
    description = "Work of a fulltime nerd"

    def items(self):
        return api.list_entries().order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.entry

    def item_link(self, item):
        return item.get_absolute_url()

