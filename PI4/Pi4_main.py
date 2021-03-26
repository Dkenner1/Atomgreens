from time import sleep
from database.db import connect
from database.SQL import PI4_STATUS
from utcp import UTCP 
from database.db import add_meas


for x in range(5): #add measurments to all of the pi0's
    add_meas(x, 1, 50) #humidity 
    add_meas(x, 2, 5.5) #temp 
    add_meas(x, 3, 10) #weight sensor  
    add_meas(x, 4, 0) #solinoid filler   
    add_meas(x, 5, 80) #red  
    add_meas(x, 6, 60) #Blue 


add_meas(0, 1, 50) #humidity 
add_meas(0, 2, 5.5) #temp 
add_meas(0, 7, 0) # air pump filler 
add_meas(0, 8, 0) # water  pump filler 
add_meas(0, 9, 0) # air pump filler 
add_meas(0, 10, 0) # EC  pump filler 
add_meas(0, 11, 0) # PH  pump filler 
add_meas(0, 12, 0) # ph sensor filler 
add_meas(0, 13, 0) # ec sensor filler 

'''
conn = connect()
cur = conn.cursor()
for row in cur.execute('SELECT val, MAX(epoch_time) FROM STATUS WHERE piID = 0 and devid = 11'): #get the latest temp value 
    PH = row
conn.close()

print (float(EC)) # [row#][col#]
'''
