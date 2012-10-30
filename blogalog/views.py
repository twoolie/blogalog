from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.sites.models import get_current_site
from django.contrib.syndication.views import Feed
from models import Entry
# Create your views here.

class VisibleFilterMixin(object):
    def get_queryset(self):
        #You can append a .filter to this!
        try:
            if self.request.user.is_authenticated():
                return super(VisibleFilterMixin,self).get_queryset()
        except AttributeError:
            pass
        return super(VisibleFilterMixin,self).get_queryset().filter(visible=True)

class OrderFilterMixin(object):
    def get_queryset(self):
        return super(OrderFilterMixin,self).get_queryset().order_by('-pub_date')

class EntryVisibleListView(OrderFilterMixin, VisibleFilterMixin, ListView):
    model = Entry

class EntryListView(OrderFilterMixin, ListView):
    model = Entry

class EntryDetailView(VisibleFilterMixin, DetailView):
    model = Entry

class EntryCreate(CreateView):
    model = Entry

class EntryUpdate(UpdateView):
    model = Entry

class LatestEntriesFeed(Feed):
    title = "Firstyear's blog-a-log"
    link = "/blog/"
    description = "Work of a fulltime nerd"

    def items(self):
        return EntryVisibleListView().get_queryset()[:5]
        #return api.list_entries().order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.entry

    def item_link(self, item):
        return item.get_absolute_url()

