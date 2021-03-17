import RPi.GPIO as GPIO
from time import sleep
#from util.db import connect, add_meas
#from util.SQL import PI4_STATUS
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

SPR = 200 # Steps per revolution
delay = 0.1

pinPHBlack = 40
pinPHGrn = 38
pinPHBlue = 32
pinPHRed = 36

pinECBlack = 37
pinECGrn = 35
pinECBlue = 31
pinECRed = 33

CTRL = 29

control_pins = [pinPHBlack, pinPHGrn, pinPHBlue, pinPHRed, pinECBlack, pinECGrn, pinECBlue, pinECRed, CTRL]
for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
GPIO.output(29, GPIO.LOW) #turns off both pumps

# Question: What is the correct value/amount (cutoff) of PH buffer and nutrient solution?
        # Placeholder values, find and insert new values here with testing 
stdValPH = 5.5
stdValEC = 250

#placeholder values, should retreive from database whenever script is called 
phPumpCount = 0
ecPumpCount = 0

class PhEcPump:
    def On(): 
        # Query database for last stored PH and EC sensor value and pump counts
        # conn = connect()
        # cur = conn.cursor()
        # data = {item[0].replace('','_'): item[1] for item in cur.execute(PI4_STATUS)}
        # conn.close()
        
        #placeholder values, should retreive from database whenever script is called 
        phPumpCount = 0
        ecPumpCount = 0

        # Store PH and EC values as local file variables
        phVal = 5.6
        #print(phVal)
        ecVal = 240
        #print(ecVal)
        pumpCnt = 2
        GPIO.output(29, GPIO.HIGH) #turn on the pumps 

        # If below cutoff, turn on respective pumps, increment pump count and write pump count value to database
            # PH pump
    #     if phVal < stdValPH:
    #         runPH = ((phVal - stdValPH) * 10) * SPR
    #         phPumpCount = ((phVal - stdValPH) * 10)
    #         # Turn on PH pump
    # 
    #         for x in range(SPR):
    #             GPIO.output(pinPHBlue, GPIO.LOW)
    #             GPIO.output(pinPHBlack, GPIO.HIGH)
    #             sleep(delay)
    #             GPIO.output(pinPHBlack, GPIO.LOW)
    #             GPIO.output(pinPHRed, GPIO.HIGH)
    #             sleep(delay)
    #             GPIO.output(pinPHRed, GPIO.LOW)
    #             GPIO.output(pinPHGrn, GPIO.HIGH)
    #             sleep(delay)
    #             GPIO.output(pinPHGrn, GPIO.LOW)
    #             GPIO.output(pinPHBlue, GPIO.HIGH)
    #     GPIO.output(pinPHGrn, GPIO.LOW)
    #     GPIO.output(pinPHBlue, GPIO.LOW)
    #     GPIO.output(pinPHGrn, GPIO.LOW)
    #     GPIO.output(pinPHBlue, GPIO.LOW)
    #     # Increment phPumpCount and insert phPumpCount value into database | Question: add_meas() function to be used?
    #     # add_meas(1,10,(pumpCnt + phPumpCount))
    #     print(pumpCnt + phPumpCount)

        # EC pump
        print(ecVal)
        print(stdValEC)
        if ecVal < stdValEC:
            revNum = ((stdValEC - ecVal)/10) * SPR
            ecPumpCount = ((stdValEC - ecVal) * 10)
            # Turn on EC pump
            print(revNum)
            for x in range(round(revNum)):
                GPIO.output(pinECBlack, GPIO.LOW)
                GPIO.output(pinECRed, GPIO.HIGH)
                sleep(delay)
                GPIO.output(pinECRed, GPIO.LOW)
                GPIO.output(pinECGrn, GPIO.HIGH)
                sleep(delay)
                GPIO.output(pinECGrn, GPIO.LOW)
                GPIO.output(pinECBlue, GPIO.HIGH)
                sleep(delay)
                GPIO.output(pinECBlue, GPIO.LOW)
                GPIO.output(pinECBlack, GPIO.HIGH)
                sleep(delay)
        GPIO.output(pinECBlack, GPIO.LOW)
        GPIO.output(pinECRed, GPIO.LOW)
        GPIO.output(pinECGrn, GPIO.LOW)
        GPIO.output(pinECBlue, GPIO.LOW)
        # Increment ecPumpCount and insert ecPumpCount value into database | Question: add_meas() function to be used?
        #add_meas(1, 9, (pumpCnt + ecPumpCount))
        GPIO.output(29, GPIO.LOW) #turn off the pumps 
