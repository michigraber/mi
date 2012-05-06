from django.views.generic.simple import direct_to_template

from mi.mimamato.models import MediaUrl


def home(request):
    '''
    '''

    return direct_to_template(request, 'home.html', {})


def webcams(request):
    '''
    '''
    mediaurls = MediaUrl.objects.filter(type=MediaUrl.TYPE_WEBCAM)

    _dict = {
        'mediaurls': mediaurls,
            }

    return direct_to_template(request, 'webcams.html', _dict)


def weather(request):
    '''
    '''

    mediaurls = MediaUrl.objects.filter(type=MediaUrl.TYPE_WEATHERFORECAST)

    _dict = {
        'mediaurls': mediaurls,
            }

    return direct_to_template(request, 'weather.html', _dict)
