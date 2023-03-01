from os import system, name

import random

def welcome(console=True, clear=True):
    if console:
        if clear: clear_console()
        
        print('##### Bienvenido a Talana Fight!! #####\n')
        print('--- Instrucciones de uso:')
        print('Para cargar las instrucciones de pelea en el programa, debe dejar el archivo JSON dentro del directorio \'json\' antes de continuar.')
        print('\n--- Formato JSON:')
        print('El JSON a cargar debe estar en el formato adecuado. De lo contrario, el programa no procesara la pelea.\nEl formato requerido es el siguiente:\n')
        print('{\'player1\': {\'movimientos\':[lista-de-movimientos], \'golpes\':[lista-de-golpes]},\'player2\': {misma-estructura-player1}}\n')
        input('\nPresione cualquier ENTER cuando este listo para iniciar...')
        
        if clear: clear_console()            
    
def clear_console():
    system('cls') if name in ['win','Windows','win32'] else system('clear')
    
def rnd_msg_movimiento():
    txt = [
        ' intenta esquivar sin exito',
        ' se mueve para tratar de despistar',
        ' se nota un poco frío. Se mueve y mira fijamente',
        ' se mueve para posicionarse cerca'
    ]
    return txt[random.randint(0, len(txt)-1)]

def rnd_msg_hit():
    txt = [
        ' conecta un ',
        ' le da un ',
        ' acierta un ',
        ' enchufa un ',
        ' da un potente ',
        ' remece de un '
    ]
    return txt[random.randint(0, len(txt)-1)]

def rnd_msg_to():
    txt = [
        ' a ',
        ' al pobre ',
        ' al desconcertado ',
        ' a ',
        ' y enfada a ',
        ' al gran ',
        ' a '
    ]
    return txt[random.randint(0, len(txt)-1)]

def rnd_msg_none():
    txt = [
        ' está exhausto! no hace más que mirar',
        ' sólo mira',
        ' está mareado... no logra enfocar'
        ' sólo espera',
        ' no está en forma! no se puede ni mover! sólo vean'
    ]
    return txt[random.randint(0, len(txt)-1)]
