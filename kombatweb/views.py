from django.shortcuts import render

import modules.archivos as ar

# Create your views here.
def index(request):
    # return HttpResponse('Hola!! Este sería mi Index.')
    # template = loader.get_template('kombatweb/index.html')
    files = ar.lista_json('kombat/static/json/')
    context = {
        "archivos" : files
    }
    return render(request, 'kombatweb.html', context)