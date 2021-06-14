import pymongo
from pymongo import MongoClient


class Database:
    def __init__(self):

        self.cluster = MongoClient("mongodb+srv://okonan:123@cluster0.8joih.mongodb.net/AirControl?retryWrites=true&w=majority")
        self.db = self.cluster["AirControl"]
        self.collection = self.db["AirControl"]
        self.TimeStr = ""
        self.COStr = ""
        self.CO2Str = ""
        self.SmokeStr = ""
        self.LPGStr = ""
        self.TempStr = ""
        self.HumStr = ""
        self.FailureStr = ""
        self.MetanStr = ""
        self.PropanStr = ""
        self.HydrogenStr = ""
        self.missed_post = None

    def prepare_data(self, SensorValArr):
        
        self.TimeStr = SensorValArr[0]
        self.LPGStr = str(SensorValArr[1]) + " ppm"
        self.MetanStr = str(SensorValArr[2]) + " ppm"
        self.PropanStr =  str(SensorValArr[3]) + " ppm"
        self.COStr = str(SensorValArr[4]) + " ppm"
        self.HydrogenStr = str(SensorValArr[5]) + " ppm"
        self.SmokeStr = str(SensorValArr[6]) + " ppm"
        self.CO2Str = str(SensorValArr[7]) + " ppm"
        
        
        self.TempStr = str(SensorValArr[8]) + " °C"
        self.HumStr = "%" + str(SensorValArr[9]) 
        self.FailureStr = str(SensorValArr[10])

    def send_data(self):
        
        if self.missed_post:
            self.collection.insert_one(missed_post)
            self.missed_post = None
            
        post = {"_id":self.TimeStr, "LPG" : self.LPGStr, "Metan":self.MetanStr, "Propan":self.PropanStr, "CO": self.COStr, "Hydrogen":self.HydrogenStr, \
                "Smoke": self.SmokeStr, "CO2" : self.CO2Str, "Temperature": self.TempStr, "Humidity": self.HumStr, "Failure": self.FailureStr}
        try:
            self.collection.insert_one(post)
        except:
            self.missed_post = post


