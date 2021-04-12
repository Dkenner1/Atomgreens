from time import sleep
from database.db import connect
from database.SQL import PI4_STATUS
from utcp import UTCP 
from database.db import add_meas
from database.paths import db_dir
from database.SQL import SELECT_NODEID, MEAS_INSRT, NODE_INSRT, select_table
import PI4_schedule
import climate_control

climate_control.control()

#add_node(0,) #piId, devId 
'''
conn = connect(db_dir) 
cur = conn.cursor() 
cur.execute('UPDATE nodes SET devId = 5 WHERE devId = 3 and piId = 0')
#for row in cur.execute('INSERT FROM nodes WHERE nodeId = 5'): 
#    print(row) 
conn.close() 
'''

'''
for x in range(1,5): #add measurments to all of the pi0's
    add_meas(x, 1, 50) #humidity 
    add_meas(x, 2, 5.5) #temp 
    add_meas(x, 3, 10) #weight sensor  
    add_meas(x, 4, 0) #solinoid filler 
    add_meas(x, 5, 80) #red 
    add_meas(x, 6, 60) #Blue 

add_meas(0, 7, 0) # air pump filler 
add_meas(0, 8, 0) # water pump filler 
add_meas(0, 9, 0) # EC pump filler 
add_meas(0, 10, 0) # PH pump filler 
add_meas(0, 15, 0) # heater filler 
add_meas(0, 16, 0) # cooler filler 

add_meas(0, 1, 50) #humidity 
add_meas(0, 2, 5.5) #temp 
add_meas(0, 11, 0) # PH sensor 
add_meas(0, 12, 0) # EC sensor 
add_meas(0, 13, 0) # water temp 
add_meas(0, 14, 1) # water level 
'''


