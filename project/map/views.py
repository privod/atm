from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext

from map.models import Atm


def index(request):
    atm_list = Atm.objects.all()
    template = loader.get_template('map/index.html')
    context = RequestContext(request, {
        'atm_list': atm_list,
    })
    return HttpResponse(template.render(context))
