import os

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests
import pusher

from .models import Greeting

# Create your views here.


def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return render(request, 'message.html', {'text': r.text})


def hello(request):
    times = int(os.environ.get('TIMES', 3))
    return render(request, 'message.html', {'text': 'Hello! ' * times})


def bla(request):
    pusher_client = pusher.Pusher(
        app_id=settings.PUSHER_APP_ID, key=settings.PUSHER_KEY, secret=settings.PUSHER_SECRET, cluster=settings.PUSHER_CLUSTER)
    pusher_client.trigger(u'a_channel', u'an_event', {
                          u'some': u'you look nice'})
    return render(request, 'message.html', {'text': 'Message sent'})


def chat(request):
    return render(request, "chat.html", {"key": "08c03b81194407aeef5c"})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def who(request):
    url = 'https://iptoearth.expeditedaddons.com'
    params = {
        'api_key': settings.IPTOEARTH_API_KEY,
        'ip': get_client_ip(request),
    }
    res = requests.get(url, params=params)
    return render(request, 'message.html', {'text': res.text})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def hello_world(request):
    return render(request, 'helloworld.html')
