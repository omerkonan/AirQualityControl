# AirQualityControl
It's a cloud air quality control project. It uses mq-2, mq-7, mq-135, mh-z19, dht-22 sensors and save data to MongoDB.
## All Cable connections
If you change GPIO input, code inputs should be updated.

![All cable connecitons](https://github.com/OmerKonan/AirQualityControl/blob/master/img/all_connections.png)
## Prerequirements
 -- Arduino IDE
 
 -- MongoDB Account
 
 -- Libraries 
 
    sudo pip3 install mh-z19
    sudo  pip3 install pymongo
    sudo  pip3 install Adafruit_DHT
    
## Copy your client URL and paste database.py line 10 and change cluster and db names.
![All cable connecitons](https://github.com/OmerKonan/AirQualityControl/blob/master/img/mongo_db_path.png)


# First load mq.ino on the arduino
# Then run 
    sudo python3 main.py
    
