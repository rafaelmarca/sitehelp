from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'siteHelp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #(r'^cadastros/$', 'cadastros.views.index'),
    #(r'^cadastros/(?P<modulo_id>\d+)/$', 'siteHelp.cadastros.views.detail'),
    url(r'^admin/', include(admin.site.urls)),

)
