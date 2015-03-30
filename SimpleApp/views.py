from django.shortcuts import render_to_response
from django.http import HttpResponse
from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter

from config import CONFIG

authomatic = Authomatic(CONFIG, 'Una super cadena de texto')

def holaMundo(request):
	return render_to_response('home.html', { 'title': 'TituloApp' })
