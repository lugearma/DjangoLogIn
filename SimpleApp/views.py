from django.shortcuts import render_to_response
from django.http import HttpResponse
from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter

from config import CONFIG

authomatic = Authomatic(CONFIG, 'Una super cadena de texto')

def home(request):
	return render_to_response('home.html', { 'title': 'TituloApp' })

def login(request, provider_name):
    response = HttpResponse()
	#Este nos trae el resultado del proceso
    result = authomatic.login(DjangoAdapter(request, response), provider_name)

    #Si existe
    if result:
        #Ahora comprobaremos, si hay error o si no lo hay
        if result.error:
            print 'Ocurrio un error'
            print result.error.message
            response.write('<h1>Ocurrio un Error</h1>' + result.error.message)
        elif result.user:
            print 'Estas logeado :)'
            response.write('<h1>Estas Logeado :)</h1>')
    return response

def simpleApp(request):
    response.write('<h1>Estas Logeado :)</h1>')
    return HttpResponse()
