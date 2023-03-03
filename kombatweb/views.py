from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

import modules.archivos as ar

# Create your views here.
def index(request):
    # return HttpResponse('Hola!! Este sería mi Index.')
    # template = loader.get_template('kombatweb/index.html')
    files = ar.lista_json('kombat/static/json/')
    context = {
        "archivos" : files,
    }
    return render(request, 'kombatweb.html', context)

def trae_contenido_json(request):
    if request.method == 'POST':
        print(request.POST["archivo"])
        respuesta = ar.json_content('kombat/static/json/', request.POST["archivo"])
        
        return JsonResponse(respuesta, status=200)
    else:
        return JsonResponse({"error": "BAD REQUEST"}, status=400)