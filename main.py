# Se importan los módulos necesarios
from os import system, name
from modules.FightPlan import FightPlan
from modules.Fight import Fight
from modules.messages import welcome
from modules.archivos import lista_json

def main():
    '''
        Este es el punto de entrada del programa.  No modifique el orden de las llamadas 
        ni la lógica del código, de lo contrario, podría alterar el correcto funcionamiento
        de la aplicación.
        
        - El archivo JSON con los movimientos y golpes, debe estar en el directorio json.
        - Para pruebas y efectos didácticos, comente las líneas de código. No las borre.
        - Si quiere obviar el mensaje de Bienvenida y saltarse la acción de presionar una tecla, comente la llamada a la función welcome()
        - Si quiere evitar que la consola se limpie después de la Bienvenida, pase el parámetro False a welcome. Ej.: welcome(False) 
    '''
    ruta_base = 'json\\' if name in ['win','Windows','win32'] else 'json/'
    
    #Mensaje de Bienvenida y primera interacción.
    welcome()
    
    json_disponibles = lista_json(ruta_base) 
    print('A continuación se listan los archivos JSON disponibles para cargar como plan de pelea.\n')
    
    max_index = 0
    
    for index,value in enumerate(json_disponibles):
        print(f'{index} - {value}')
        max_value = index
        
        if index == 9: break
        
    print('10 - Salir')
    
    index_archivo = ''
    
    while not(index_archivo.isnumeric()):
        index_archivo = input('\nIngrese el número del archivo que desea usar: ')

    if int(index_archivo) == 10:
        print('Adiós!')
        return False
    
    #Se inicializa la Clase que prepara el plan de pelea.
    pre_fight = FightPlan(json_disponibles[int(index_archivo)],'',ruta_base)
    
    #Se inicializa la Clase de pelea e inicia la secuencia
    fight = Fight(pre_fight.fighters)

#Entrada
main()