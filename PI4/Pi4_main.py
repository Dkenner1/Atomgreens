from time import sleep
from database.db import connect
from database.SQL import PI4_STATUS

conn = connect()
cur = conn.cursor()
for row in cur.execute('SELECT val, MAX(epoch_time) FROM STATUS WHERE piID = 0 and devid = 11'): #get the latest temp value 
    PH = row
for row in cur.execute('SELECT val, MAX(epoch_time) FROM STATUS WHERE piID = 0 and devid = 12'): #get the latest temp value 
    EC = row
conn.close()

print (float(EC)) # [row#][col#]
print (float(PH)) # [tray#][val(not epoch time)]
