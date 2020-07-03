import serial

class Cummunication: 
    """
    It's a class for serial communication between Arduino and Rapsberry PI
    """
    
    def __init__(self):
        self.portpath = "/dev/ttyACM1"
        self.boudrate = 115200
        self.timeout = 1
        self. stopbits = 1.5
        self.msgID = 0 # 0 means there is no message
                           # 1 means it is LPG
                           # 2 means it is Smoke
                           # 3 means it is CO
    
    def connect(self):
        """
        The method is for conneting serial port 115200.
        The port should close after using with port.close() command.
        """
        port = serial.Serial(self.portpath, self.boudrate, \
                             timeout = self.timeout, stopbits = self.stopbits)
        return port
            
    def read_message(self, port):
        
        """
        The method is for reading port line by line.
        It is going to return lastest line of port.
        """
        ValueByte = port.readline()
        ValueStr = str(ValueByte)
        ValueStr = ValueStr.replace('b', '')
        ValueStr = ValueStr.replace('\'','')
        print(ValueStr)
        return ValueStr
        
    def getValue(self, ValueStr):
    """
    The method is for classifying message line.
    Then it is going to return sensor value as a integer and messageID.
    """

        val = 0
        self.msgID = 0
        if ValueStr.find("LPG") != -1:
            ValArr = ValueStr.split(":")[1].split("ppm")
            val = int(ValArr[0])
            self.msgID = 1
            #print("Read LPG:", val)
        if ValueStr.find("SMOKE") != -1:
            ValArr = ValueStr.split(":")[1].split("ppm")
            val = int(ValArr[0])
            self.msgID = 2
            #print("Read Smoke:", val)
        if ValueStr.find("CO") != -1:
            ValArr = ValueStr.split(":")[1].split("ppm")
            val = int(ValArr[0])
            self.msgID = 3
            #print("Read CO:", val)
            
        return val, self.msgID

