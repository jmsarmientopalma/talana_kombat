from pathlib import Path
import json


def lista_json(ruta_json):
    archivos_json = []
    basepath = Path(ruta_json)    
    json_files = (archivo for archivo in basepath.iterdir() if archivo.is_file())
    
    for item in json_files:
        archivos_json.append(item.name)
    return archivos_json    


def json_content(ruta,archivo):
    with open(ruta+archivo, 'r') as archivo:
        return json.load(archivo)
    

def save_json_file(ruta,file):
    with open(ruta+file.name, 'wb+') as arch:
        for chunk in file.chunks():
            arch.write(chunk)   