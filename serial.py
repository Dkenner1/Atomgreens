from time import sleep
import serial

# soloTree is the temporary dataframe which will be sent to a CSV file every time we move onto a new feature
#soloTree = featurelist[0:0]
# ^sets solotree to be an empty datadrame^

ser = serial.Serial("/dev/ttyS0", 9600)  # Open port with baud rate
while True:
    ser.write(b'h')
    sleep(1)
    received_data = ser.read()  # read serial port
    data_left = ser.inWaiting()  # check for remaining byte
    received_data += ser.read(data_left)