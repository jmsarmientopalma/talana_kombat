from os import system, name
from time import sleep
from django.shortcuts import render
from django.http import StreamingHttpResponse

from modules import Fight, FightPlan

# Create your views here.
def show_fight(request):
    ruta_base = 'kombat\\static\\json\\' if name in ['win','Windows','win32'] else 'kombat/static/json/'
    
    #Se inicializa la Clase que prepara el plan de pelea.
    pre_fight = FightPlan(request.POST["archivo"],'',ruta_base)
    
    #Se inicializa la Clase de pelea e inicia la secuencia
    fight = Fight(pre_fight.fighters)
    
    # for msg in fight.sse_move_list:
    #     sleep(1)
        
    return StreamingHttpResponse(fight.sse_move_list, content_type='text/event-stream')
        
    