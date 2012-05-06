from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('mi.mimamato.views.mimamato_main',

    url(r'^$', 'home', {}, 'mimamato_home'),
    url(r'^webcams/', 'webcams', {}, 'mimamato_webcams'),
)


# Uncomment these two lines to enable your static files on PythonAnywhere
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#urlpatterns += staticfiles_urlpatterns()