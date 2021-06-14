import dht22
import comm
import mh_z19
from datetime import datetime
import comm
from constants import *
from database import *
def getTime():
    now = datetime.now()
    dt_str = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_str)
    return dt_str

def main():


    TIME = getTime()
    SensorValueArr = [TIME, LPG, METAN, PROPAN, CO, HYDROGEN, SMOKE, CO2, TEMP, HUM, FAILURE]
    db = Database()      
    com = comm.Cummunication()
    port = com.connect()
    dht22_sensor = dht22.DHT22()
    while(True):
        
        msg = com.read_message(port)
        val, msgID  = com.getValue(msg)
        print ("value:", val)
        print("type:", msgID)
        if msgID != 0:
            SensorValueArr[7] = mh_z19.read()["co2"]
            SensorValueArr[8] = dht22_sensor.read_dht(False)
            SensorValueArr[9] = dht22_sensor.read_dht(True)
            SensorValueArr[msgID] = val
            if SensorValueArr[1] >= LPG_LIMIT and SensorValueArr[2] >= METAN_LIMIT and \
               SensorValueArr[3] >= PROPAN_LIMIT and SensorValueArr[4] >= CO_LIMIT and \
               SensorValueArr[5] >= HYDROGEN_LIMIT and SensorValueArr[6] >=SMOKE_LIMIT and \
               SensorValueArr[7] >= CO2_LIMIT and SensorValueArr[8] >= TEMP_LIMIT and SensorValueArr[9] >= HUM_LIMIT:
                SensorValueArr[10] = True
         
        if msgID == 6:
            msgID = 0
            SensorValueArr[0] = getTime()
            db.prepare_data(SensorValueArr)
            db.send_data()
            print("Data sent...")
        
        print(SensorValueArr)
        



if __name__ == "__main__":
    main()