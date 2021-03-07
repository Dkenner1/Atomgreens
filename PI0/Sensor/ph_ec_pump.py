import RPi.GPIO as GPIO
from time import sleep
#from util.db import connect, add_meas
#from util.SQL import PI4_STATUS

class PhEcPump:

    GPIO.setmode(GPIO.BOARD)

    SPR = 200 # Steps per revolution
    delay = 0.0001
    pinPHBlue = 38
    pinPHGrn = 40
    pinECGrn = 28
    pinECBlue = 26

    control_pins = [pinPHBlue, pinPHGrn, pinECGrn, pinECBlue]
    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)

    # Question: What is the correct value/amount (cutoff) of PH buffer and nutrient solution?
    # Placeholder values
    stdValPH = 5.5
    stdValEC = 250

    phPumpCount = 0
    ecPumpCount = 0

    # Query database for last stored PH and EC sensor value and pump counts
    # conn = connect()
    # cur = conn.cursor()
    # data = {item[0].replace('','_'): item[1] for item in cur.execute(PI4_STATUS)}
    # conn.close()

    # Store PH and EC values as local file variables
    phVal = 5.6
    #print(phVal)
    #ecVal = 26
    #print(ecVal)
    pumpCnt = 2

    # If below cutoff, turn on respective pumps, increment pump count and write pump count value to database
        # PH pump
    if phVal < stdValPH:
        runPH = ((phVal - stdValPH) * 10) * SPR
        phPumpCount = ((phVal - stdValPH) * 10)
        # Turn on PH pump

        for x in range(SPR):
            GPIO.output(pinPHBlue, GPIO.LOW)
            GPIO.output(pinPHGrn, GPIO.HIGH)
            sleep(delay)
            GPIO.output(pinPHGrn, GPIO.LOW)
            GPIO.output(pinPHBlue, GPIO.HIGH)
    GPIO.output(pinPHGrn, GPIO.LOW)
    GPIO.output(pinPHBlue, GPIO.LOW)
    # Increment phPumpCount and insert phPumpCount value into database | Question: add_meas() function to be used?
    # add_meas(1,10,(pumpCnt + phPumpCount))
    print(pumpCnt + phPumpCount)

    # EC pump
    #if ecVal < stdValEC:
        #ecPH = ((ecVal - stdValEC)/10) * SPR
        #ecPumpCount = ((ecVal - stdValEC) * 10)
        # Turn on EC pump
        #for x in range(SPR):
            #GPIO.output(pinECGrn, GPIO.LOW)
            #GPIO.output(pinECBlue, GPIO.HIGH)
            #sleep(delay)
            #GPIO.output(pinECBlue, GPIO.LOW)
            #GPIO.output(pinECGrn, GPIO.HIGH)

    # Increment ecPumpCount and insert ecPumpCount value into database | Question: add_meas() function to be used?
    #add_meas(1, 9, (pumpCnt + ecPumpCount))




