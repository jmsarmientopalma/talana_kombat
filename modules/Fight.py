import time
import random
import itertools as itr

class Fight():
    
    def __init__(self,fighters):
        from modules.messages import rnd_msg_hit, rnd_msg_movimiento, rnd_msg_to, rnd_msg_none
        self.fighters = fighters
        self.rnd_msg_hit = rnd_msg_hit
        self.rnd_msg_movimiento = rnd_msg_movimiento
        self.rnd_msg_to = rnd_msg_to
        self.rnd_msg_none = rnd_msg_none
        self.fight()
        
    def first_move_msg(self,figther_name):
        print(f'\n{figther_name} toma la iniciativa e inicia la pelea!\n')
        return True
        
    def check_special(self,moves,specials):
        #Validación para cuando uno de los peleadores viene con menos movimientos
        if moves is None : return [self.rnd_msg_none(),0]
        
        #Validación y atajo para cuando el peleador no golpea
        if moves[1].strip() == '': return [self.rnd_msg_movimiento(),0]
        
        for sp in specials:
            if sp['mov'].strip() == '':
                continue
            
            # print(moves[0].strip())
            # print(sp['mov'].strip())
            
            if moves[0].strip().endswith(sp['mov'].strip()) and moves[1].strip() == sp['golpe'].strip():
                return [self.rnd_msg_hit()+sp['name'],sp['damage']]
        
        #Llegado a este punto, el peleador no lanzará ningún ataque especial, por lo que debe ser puño o patada
        # return list(filter(lambda g : g['golpe'].strip().upper() == moves[1].strip().upper() , specials))
        for hit in specials:
            if hit['golpe'].strip().upper() == moves[1].strip().upper():
                return [self.rnd_msg_hit()+hit['name'],hit['damage']]
    
    def fight(self):
        if self.first_move_msg(dict(list(filter(lambda f : f['starter'] == True, self.fighters))[0])['name']): self.movimientos()
    
    def movimientos(self):
        primero = dict(list(filter(lambda f : f['starter'] == True, self.fighters))[0])
        segundo = dict(list(filter(lambda f : f['starter'] == False, self.fighters))[0])
        
        #Se aprovecha esta instancia para guardar el máximo de vida
        self.max_life = primero['life']
        
        mov_primero = list(zip(primero['movimientos'],primero['golpes']))
        spe_primero = primero['tech']
        mov_segundo = list(zip(segundo['movimientos'],segundo['golpes']))
        spe_segundo = segundo['tech']
        
        for (attacker1,attacker2) in itr.zip_longest(mov_primero, mov_segundo):
            tmp_list_hit = self.check_special(attacker1, spe_primero)
            print('- '+primero['name']+str(tmp_list_hit[0])+self.rnd_msg_to()+segundo['name']+'\n')
            segundo['life'] = segundo['life'] - tmp_list_hit[1]
            
            if segundo['life'] <= 0:
                self.msg_win(primero)
                return True
            
            time.sleep(2)
           
            tmp_list_hit = self.check_special(attacker2, spe_segundo)
            print('- '+segundo['name']+str(tmp_list_hit[0])+self.rnd_msg_to()+primero['name']+'\n')
            primero['life'] = primero['life'] - tmp_list_hit[1]
            
            if primero['life'] <= 0:
                self.msg_win(segundo)
                return True
            
            time.sleep(2)
            
    
    def msg_win(self,winner):
        if winner['life'] == self.max_life:
            print(f'PERFECT para {winner["name"]}!!!')
        elif winner['life'] == int(winner['life'] / 2):
            print(f'{winner["name"]} gana la pelea quedando con {int(winner["life"] / 2)} puntos de vida.')
        elif winner['life'] == 2:
            print(f'En una emocionante pelea, {winner["name"]} gana quedando con 2 puntos de vida.')
        elif winner['life'] == 1:
            print(f'INCREÍBLE!! {winner["name"]} gana la pelea en el último momento quedando con 1 punto de vida!')
        else:
            print(f'{winner["name"]} a ganado la pelea quedando con {winner["life"]} puntos de vida.')
            
        
        
        