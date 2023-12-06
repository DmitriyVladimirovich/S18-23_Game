from pynput import keyboard
from map import Map
import time
import os
from helicopter import Helicopter as Hel
from clouds import Clouds


TICK_SLEEP=1
TREE_UPDATE=50
FIRE_UPDATE=100
CLOUDS_UPDATE=300
MAP_W,MAP_H=20,10

field = Map(MAP_W,MAP_H)
hel=Hel(MAP_W,MAP_H)
clouds=Clouds(MAP_W,MAP_H)

tick=1

MOVES={'w':(-1,0), 'd':(0,1), 's':(1,0), 'a':(0,-1)}
def process_key(key):
    global hel
    c=key.char.lower()
    if c in MOVES.keys():
        dx,dy=MOVES[c][0], MOVES[c][1]
        hel.move(dx,dy)
    
listener = keyboard.Listener(
    on_press=None,
    on_release=on_release)
listener.start()

while True:
    o.system('cls')
	field.process_helicopter(hel,clouds)
    hel.print_stats()
    field.print_map(hel,clouds)
    print('Tick:',tick)
	tick+=1
	time.sleep(TICK_SLEEP)
    if (tick%TREE_UPDATE==0):
        field.generate_tree()
    if (tick%FIRE_UPDATE==0):
        field.update_fires()
    if (tick%CLOUDS_UPDATE==0):
        clouds.update()