from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_blog.views.home', name='home'),
    # url(r'^django_blog/', include('django_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name' : 'blogalog/login.html'}, name='login' ),
    url(r'^blog/', include('blogalog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rpc$', 'rpc4django.views.serve_rpc_request'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
        (r'static/(?P<path>.*)', 'serve', {'document_root': settings.STATIC_ROOT}),
    )

