 
#!/usr/bin/python

import Adafruit_DHT
class DHT22:
    def __init__(self, pin = 4):
        self.humidity = 0
        self.temperature = 0
        self.pin = pin
        self.sensor = Adafruit_DHT.DHT11
    def read_dht(self, returnType):
        #print(Adafruit_DHT.read_retry(self.sensor, self.pin))
        while(True):
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
            if returnType == True:
                return humidity
            if returnType == False:
                return temperature


###Test###

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
"""
pin = '4'
sensor = DHT22()
val = sensor.read_dht(False)
print(val)
"""
###Test####