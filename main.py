from map import Map
import time
import os

TICK_SLEEP=50
FIRE_UPDATE=100
MAP_W,MAP_H=20,10

field = Map(MAP_W,MAP_H)
field.generate_forest(4,10)
field.generate_river(10)
field.generate_river(15)
field.add_fire()
field.print_map()

tick=1

while True:
    o.system('cls')
	print('Tick:',tick)
    field.print_map()
	tick+=1
	time.sleep(TICK_SLEEP)
    if (tick%TREE_UPDATE==0):
        field.generate_tree()
    if (tick%FIRE_UPDATE==0):
        field.update_fires()