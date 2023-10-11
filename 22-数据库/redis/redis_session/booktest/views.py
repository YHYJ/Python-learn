from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def session_set(request):
    request.session['name'] = 'YJ1516'
    return HttpResponse('ok')


def session_get(request):
    name = request.session['name']
    return HttpResponse(name)
