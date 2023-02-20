def lista_json(ruta_json):
    from pathlib import Path
    
    archivos_json = []
    basepath = Path(ruta_json)    
    json_files = (archivo for archivo in basepath.iterdir() if archivo.is_file())
    
    for item in json_files:
        archivos_json.append(item.name)
    return archivos_json    