import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

SDA = 3
SLC = 5
TEC_Perisoltic = 7
Fan = 11
PH_on = 13
EC_on = 15
Din = 19 #Pi4 output
Dout = 21 #Pi4 input
SCLK = 23
Step_CTRL = 29
EC_Blue = 31
EC_Red = 33
RC_Grn = 35
EC_Black = 37

TX = 8
RX = 10 # input 
heater = 12
Float = 16 #input
water_pump = 18
Air_pump = 22
ADC_CS = 24 #put high
PH_Blue = 32
PH_Red = 36
PH_Grn = 38
PH_Black = 40 
global control_pins
control_pins = [SDA, SLC, TEC_Perisoltic, Fan, PH_on, EC_on, Din, SCLK, Step_CTRL,
                EC_Blue, EC_Red, RC_Grn, EC_Black, TX, heater, water_pump, Air_pump,
                PH_Blue, PH_Red, PH_Grn, PH_Black]
def off():
    global control_pins
    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(ADC_CS, GPIO.OUT)
        
    for pin in control_pins:
        GPIO.output(pin, GPIO.LOW)  
    GPIO.output(ADC_CS, GPIO.HIGH)
