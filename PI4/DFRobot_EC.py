import time
import sys

_kvalue                 = .987
_kvalueLow              = 1.0728
_kvalueHigh             = 1.0687
_voltage                = 0.0
_temperature            = 25.0

def readEC(voltage,temperature):
    global _kvalue
    global _kvalueLow
    global _kvalueHigh
    global _voltage
    global _temperature
    voltage = voltage*1000
    
    rawEC = 1000*voltage/820.0/200.0
    valueTemp = rawEC * _kvalue
    if(valueTemp > 2.5):
        _kvalue = _kvalueHigh
    elif(valueTemp < 2.0):
        _kvalue = _kvalueLow
    value = rawEC * _kvalue
    value = value / (1.0+0.0185*(temperature-25.0))
    formatted_string = "{:.5f}".format(value)
    EC = float(formatted_string)
    EC = EC*640
    return EC


