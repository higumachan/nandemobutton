# -*-coding: utf-8

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r"^index/$", 'myapps.buttons.views.index'),
    url(r"^button_delete/(?P<button_id>[0123456789]+)/$", 'myapps.buttons.views.button_delete'),
    url(r"^button_post/$", 'myapps.buttons.views.button_post'),
    url(r"^button_display_page/(?P<button_id>[0123456789]+)/$", 'myapps.buttons.views.button_display_page'),
    url(r"^button_display_json/(?P<button_id>[0123456789]+)/$", 'myapps.buttons.views.button_display_json'),
    url(r"^button_controler/(?P<button_id>[0123456789]+)/$", 'myapps.buttons.views.button_controler'),
    url(r"^get_like_hist_json/(?P<button_id>[0123456789]+)/$", 'myapps.buttons.views.get_like_hist_json'),
    url(r"^like_post/(?P<button_id>[0123456789]+)/$", 'myapps.buttons.views.like_post'),
)
