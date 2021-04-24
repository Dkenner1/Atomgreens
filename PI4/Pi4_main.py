import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#import climate_control
#import ph_ec_pump
from time import sleep
import ph_ec_sensors
import ADC_callable
import water_pump_ctrl
import ph_ec_pump
from database.db import add_meas

add_meas(0, 11, 8)
ph_ec_pump.On()

#GPIO.output(13, GPIO.LOW)

#water_pump_ctrl.water(1)
ph_ec_sensors.readPHEC()
'''
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, GPIO.HIGH)
sleep(5)
test = ADC_callable.call(0)
print(test)
temperature = (74.4921 / (test-3.3)) + 70.1467
print(temperature)
GPIO.output(15, GPIO.LOW)
'''
#ph_ec_pump.On()
#climate_control.control()









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


