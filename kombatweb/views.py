from os import system, name
from time import sleep
from django.shortcuts import render
from django.http import JsonResponse, StreamingHttpResponse
from django.core import serializers

import modules.archivos as ar
from modules.FightPlan import FightPlan
from modules.Fight import Fight

ruta_base = 'kombatweb\\static\\json\\' if name in ['win','Windows','win32'] else 'kombatweb/static/json/'

# Create your views here.
def index(request):
    files = ar.lista_json(ruta_base)
    context = {
        "archivos" : files,
    }
    return render(request, 'kombatweb.html', context)

def trae_contenido_json(request):
    if request.method == 'POST':
        print(request.POST["archivo"])
        respuesta = ar.json_content(ruta_base, request.POST["archivo"])
        
        request.session["file_name"] = request.POST["archivo"]
        
        return JsonResponse(respuesta, status=200)
    else:
        return JsonResponse({"error": "BAD REQUEST"}, status=400)
    
def show_fight(request):
    archivo = request.session.get("file_name",'ejemplo1.json')
    
    #Se inicializa la Clase que prepara el plan de pelea.
    pre_fight = FightPlan(archivo, '', ruta_base, False)
    
    #Se inicializa la Clase de pelea e inicia la secuencia
    fight = Fight(pre_fight.fighters, False)
    
    def event_stream():
        for move in fight.sse_move_list:
            sleep(1)
            yield f'event:comment\ndata: {move}\n\n'
        
        yield 'event:exit\ndata:Fin de la pelea\n\n'
        
    return StreamingHttpResponse(
        event_stream(), 
        content_type = 'text/event-stream',
        headers = {'Cache-Control' : 'no-cache'}
    )