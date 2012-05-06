from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('mi.mimamato.views.mimamato_main',

    url(r'^$', 'home', {}, 'mimamato_home'),
    url(r'^webcams/', 'generic_remotecontent', {'site': 'webcams', }, 'mimamato_webcams'),
    url(r'^wetter/', 'generic_remotecontent', {'site': 'weather', }, 'mimamato_weather'),
    url(r'^logbuch/', 'home', {}, 'mimamato_logbook'),

)


# Uncomment these two lines to enable your static files on PythonAnywhere
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#urlpatterns += staticfiles_urlpatterns()
