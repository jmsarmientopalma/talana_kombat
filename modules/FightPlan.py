import json
import time

class FightPlan():
    json_raw = ''
    fighter_life = 6
    techniques_tonyn = [
        {'mov' : ''    , 'golpe' : 'P', 'damage' : 1, 'name' : 'Puñetazo'},
        {'mov' : ''    , 'golpe' : 'K', 'damage' : 1, 'name' : 'Patadón'},
        {'mov' : 'DSD' , 'golpe' : 'P', 'damage' : 3, 'name' : 'Taladoken'},
        {'mov' : 'SD'  , 'golpe' : 'K', 'damage' : 2, 'name' : 'Remuyuken'},
    ]
    
    techniques_arnaldor = [
        {'mov' : ''    , 'golpe' : 'P', 'damage' : 1, 'name' : 'Gancho'},
        {'mov' : ''    , 'golpe' : 'K', 'damage' : 1, 'name' : 'Patadón'},
        {'mov' : 'SA'  , 'golpe' : 'K', 'damage' : 3, 'name' : 'Remuyuken'},
        {'mov' : 'ASA' , 'golpe' : 'P', 'damage' : 2, 'name' : 'Taladoken'}
    ]
    
    def __init__(self,nombre_json,cadena_json,ruta_base='static/json/'):
        self.nombre_json = nombre_json
        self.cadena_json = cadena_json
        self.ruta_base = ruta_base
        
        if self.nombre_json.strip() != '':
            try:
                if self.read_file(): self.prepare_fighters()
            except ValueError as err:
                self.exit_error(err)
    
    def read_file(self):
        with open(self.ruta_base+self.nombre_json) as file:
            self.json_raw = json.load(file)
        return self.json_raw
            
    def prepare_fighters(self):
        try:
            self.tonyn,self.arnaldor = [self.json_raw['player1'],self.json_raw['player2']]
            # self.helper_print()
            self.tonyn['name'] = 'Tonyn'
            self.tonyn['tech'] = self.techniques_tonyn
            self.tonyn['life'] = self.fighter_life
            self.arnaldor['name'] = 'Arnaldor'
            self.arnaldor['tech'] = self.techniques_arnaldor
            self.arnaldor['life'] = self.fighter_life
            print('Peleadores preparados...!')
            self.bell()
        except Exception as err:
            print('Los peleadores no se sienten preprados...')
            self.exit_error('Los planes de pelea no son adecuados. Selecciones otro JSON.')
        
    
    
    def starting_fighter(self):
        #Se determina quién inicia la pelea, según la cantidad de movimientos y de golpes
        #Se eliminan elementos vacíos.
        p1_count = len(''.join(list(filter(None, self.tonyn['movimientos']+self.tonyn['golpes']))))
        p2_count = len(''.join(list(filter(None, self.arnaldor['movimientos']+self.arnaldor['golpes']))))
        
        if p1_count == p2_count:
            p1_count = len(''.join(list(filter(None, self.tonyn['movimientos']))))
            p2_count = len(''.join(list(filter(None, self.arnaldor['movimientos']))))
            
            if p1_count == p2_count:
                p1_count = len(''.join(list(filter(None, self.tonyn['golpes']))))
                p2_count = len(''.join(list(filter(None, self.arnaldor['golpes']))))
                
                if p1_count > p2_count:
                    # self.starter = [1,'player2','Arnaldor']
                    self.arnaldor['starter'] = True
                    self.tonyn['starter'] = False
                else:
                    # self.starter = [0,'player1','Tonyn']
                    self.arnaldor['starter'] = False
                    self.tonyn['starter'] = True
                    
            elif p1_count > p2_count:
                self.arnaldor['starter'] = True
                self.tonyn['starter'] = False
            else:
                self.arnaldor['starter'] = False
                self.tonyn['starter'] = True
                
        elif p1_count > p2_count:
            self.arnaldor['starter'] = True
            self.tonyn['starter'] = False
        else:
            self.arnaldor['starter'] = False
            self.tonyn['starter'] = True
        
        return [self.tonyn,self.arnaldor]
    
    def bell(self):
        contador = 3
        time.sleep(1)
        
        while contador:
            print(f'{contador}...')
            time.sleep(1)
            contador = contador-1
            
        print('\nFIGHT!!')
        time.sleep(1)
        
        self.fighters = self.starting_fighter()
        # print(self.json.dumps(self.fighters, indent=2))
        time.sleep(0.5)
        return True
        
    def exit_error(self, error):
        print(f'Han ocurrido errores en la ejecucion, por lo que el programa terminara ahora.\nRevise el formato JSON.\n\nMensaje de Error: {error}')
        return False
            
    def helper_print(self):
        print('CONTENIDO DEL ATRIBUTO JSON RAW---\n\n')
        print(self.json.dumps(self.json_raw, indent=2))
        print('Type:-----\n')
        print(type(self.json_raw))
        print('Movimientos--------\n')
        print(f'Player1 (Tonyn) Fight Plan : {self.tonyn}\n')
        print(f'Player2 (Arnaldor) Fight Plan : {self.arnaldor}\n')