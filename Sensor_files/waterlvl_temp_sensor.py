import sqlite3
import db
import RPi.GPIO as GPIO

    def waterConnection():
        conn = connect()
        cur = conn.cursor()
        data = {item[0].replace(' ', '_'): item[1] for item in cur.execute(PI4_STATUS)}
        conn.close()

    def waterRead():
        {% if status.water_level is defined and status.water_level < 50 %}


    # Temperature sensor


    # Water level sensor
        # Query database for water level reading of "full" or "low" | Question: What is range of full?