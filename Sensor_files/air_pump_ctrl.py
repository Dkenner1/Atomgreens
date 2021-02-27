# air_pump_ctrl.py
import RPi.GPIO as GPIO


def air_on():
    GPIO.output(airPump, GPIO.HIGH)
    print("Dispensing air...")


class AirPumpCtrl:
    GPIO.setmode(GPIO.BOARD)

    # GPIO pin for air pump
    airPump = 25
    GPIO.setup(airPump, GPIO.OUT)

    # Function for turning air pump on

