import serial

class Cummunication:
    
    def __init__(self):
        self.portpath = "/dev/ttyACM0"
        self.boudrate = 115200
        self.timeout = 1
        self. stopbits = 1.5
        self.msgID = 0 # 0 means there is no message
                           # 1 means it is LPG
                           # 2 means it is Smoke
                           # 3 means it is CO
    
    def connect(self):
        port = serial.Serial(self.portpath, self.boudrate, \
                             timeout = self.timeout, stopbits = self.stopbits)
        return port
            
    def read_message(self, port):
        
        ValueByte = port.readline()
        ValueByte = ValueByte.rstrip()
        ValueStr = str(ValueByte)
        ValueStr = ValueStr.replace('b', '')
        ValueStr = ValueStr.replace('\'', '')
        return ValueStr
        
    def getValue(self, ValueStr):
        val = 0
        self.msgID = 0
        
        if ValueStr.find("mq2") != -1:
            ValArr = ValueStr.split(":")
            val = int(ValArr[1])
            self.msgID = 1
            print("Read mq2:", val)
        if ValueStr.find("mq4") != -1:
            ValArr = ValueStr.split(":")
            val = int(ValArr[1])
            self.msgID = 2
            print("Read mq4:", val)
        if ValueStr.find("mq6") != -1:
            ValArr = ValueStr.split(":")
            val = int(ValArr[1])
            self.msgID = 3
            print("Read mq6:", val)
        if ValueStr.find("mq7") != -1:
            ValArr = ValueStr.split(":")
            val = int(ValArr[1])
            self.msgID = 4
            print("Read mq7:", val)
        if ValueStr.find("mq8") != -1:
            ValArr = ValueStr.split(":")
            val = int(ValArr[1])
            self.msgID = 5
            print("Read mq8:", val)
        if ValueStr.find("mq135") != -1:
            ValArr = ValueStr.split(":")
            val = int(ValArr[1])
            self.msgID = 6
            print("Read 135:", val)
            
        return val, self.msgID

