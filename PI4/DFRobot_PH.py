import time
import sys

_acidVoltage     = 1998.0
_neutralVoltage  = 1473.0
def readPH(voltage):
    global _acidVoltage
    global _neutralVoltage
    voltage = voltage*1000
    slope     = (7.0-4.0)/((_neutralVoltage-1500.0)/3.0 - (_acidVoltage-1500.0)/3.0)
    intercept = 7.0 - slope*(_neutralVoltage-1500.0)/3.0
    _phValue  = slope*(voltage-1500.0)/3.0+intercept
    round(_phValue,2)
    return _phValue
