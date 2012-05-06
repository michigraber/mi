from django.views.generic.simple import direct_to_template

from mi.mimamato.models import MediaUrl

def home(request, site=None):
    '''
    '''
    
    _dict = {
            }

    return direct_to_template(request, 'home.html', _dict)


def generic_remotecontent(request, site=None):
    '''
    '''
    
    type_restriction = {
            'weather' : MediaUrl.TYPE_WEATHERFORECAST,
            'webcams' : MediaUrl.TYPE_WEBCAM,
            }

    mediaurls = MediaUrl.objects.filter(type=type_restriction[site])

    _dict = {
        'site' : site, 
        'mediaurls': mediaurls,
            }

    return direct_to_template(request, 'generic_remotecontent.html', _dict)
