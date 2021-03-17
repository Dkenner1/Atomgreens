import RPi.GPIO as GPIO
import ph_ec_pump
import ADC_callable
PHVal = ADC_callable.ADC.call(2)
print(PHVal)
# from time import sleep
# import serial
# import configparser 
# from Serial.EventHub import eventHub
# from Serial.listener import listen
# import utcp
# import pwm_callable
# import weight_sensor
# import Temp_and_humidity_sensor
# import Solinoid
# 
# eventHub.subscribe(Temp_and_humidity_sensor.TH.read_temp_humidity, 1)
# eventHub.subscribe(Temp_and_humidity_sensor.TH.read_temp_humidity, 2)
# eventHub.subscribe(weight_sensor, 3)
# eventHub.subscribe(Solinoid, 4)
# eventHub.subscribe(pwm_callable.setPWM.recive(msg), 5)
# eventHub.subscribe(pwm_callable.setPWM.recive(msg), 6)
