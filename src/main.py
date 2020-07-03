import dht22
import comm
import mh_z19
from datetime import datetime
import comm
from constants import *
from database import *

def getTime():
    """
    It is going to return date and time as a string.
    """
    now = datetime.now()
    dt_str = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_str)
    return dt_str

def main():


    TIME = getTime() # Initialize time value
    SensorValueArr = [TIME, LPG, SMOKE, CO, CO2, TEMP, HUM, FAILURE] # Sensor arr keep all sensor data, time and failure data to send cloud.
    db = Database()      
    com = comm.Cummunication()
    port = com.connect()
    dht22_sensor = dht22.DHT22()
    while(True):
        
        msg = com.read_message(port)
        val, msgID  = com.getValue(msg)
        print ("value:", val)
        print("type:", msgID)
        if msgID != 0: # if the mqsensor data was read, other sensor's data will read.
            SensorValueArr[4] = mh_z19.read()["co2"]
            SensorValueArr[5] = dht22_sensor.read_dht(False)
            SensorValueArr[6] = dht22_sensor.read_dht(True)
            SensorValueArr[msgID] = val
            if SensorValueArr[1] >= LPG_LIMIT and SensorValueArr[2] >= SMOKE_LIMIT and \    
               SensorValueArr[3] >= CO_LIMIT and SensorValueArr[4] >= CO2_LIMIT and \
               SensorValueArr[5] >= TEMP_LIMIT and SensorValueArr[6] >= HUM_LIMIT: # Check Sensor failure limits.
                
                SensorValueArr[7] = True
         
        if msgID == 3: # When All sensor data was read. The data will send cloud.  
            msgID = 0
            SensorValueArr[0] = getTime()
            db.prepare_data(SensorValueArr)
            db.send_data()
            print("Data sent...")
        
        print(SensorValueArr)
        



if __name__ == "__main__":
    main()