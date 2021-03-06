# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 23:44:40 2021

@author: Muzaffer
"""

from pymongo import MongoClient

client = MongoClient()

ConnectDB = client.AirQuality    # Connect to database
ConnectCol = ConnectDB.AirQuality # Connect to collection

PM10 = ConnectCol.find({},{"_id":0,"PM10":1}) 

def FindConstants(Cp):
    
    if Cp>0 and Cp<54:
        IHi = 50
        ILo = 0
        BPHi = 54
        BPLo = 0
        return IHi, ILo,BPHi, BPLo
    
    elif Cp>55 and Cp<154:
        IHi = 100
        ILo = 51
        BPHi = 154
        BPLo = 55
        return IHi, ILo,BPHi, BPLo
    
    elif Cp>155 and Cp<254:
        IHi = 150
        ILo = 101
        BPHi = 254
        BPLo = 155
        return IHi, ILo,BPHi, BPLo    

    elif Cp>255 and Cp<354:
        IHi = 200
        ILo = 151
        BPHi = 354
        BPLo = 255
        return IHi, ILo,BPHi, BPLo   

    elif Cp>355 and Cp<424:
        IHi = 300
        ILo = 201
        BPHi = 424
        BPLo = 355
        return IHi, ILo,BPHi, BPLo

    elif Cp>425 and Cp<504:
        IHi = 400
        ILo = 301
        BPHi = 504
        BPLo = 425
        return IHi, ILo,BPHi, BPLo        
    
    elif Cp>505 and Cp<604:
        IHi = 500
        ILo = 401
        BPHi = 604
        BPLo = 505
        return IHi, ILo,BPHi, BPLo
    
    else:
        print("We have an error!")
        

def IndexMessage(AQI):
    if AQI>=0 and AQI<=50:
        return "Good"
    elif AQI>=51 and AQI<=100:
        return "Moderate"
    elif AQI>=101 and AQI<=150:
        return "Unhealthy for Sensitive Groups"
    elif AQI>=151 and AQI<=200:
        return "Unhealthy"
    elif AQI>=201 and AQI<=300:
        return "Very unhealthy"
    elif AQI>=301 and AQI<=500:
        return "Hazardous"
    else:
        return "We have an error!"

def AQI(IHi, ILo, BPHi, BPLo, Cp): # Calculate Air Quality Index
    Ip = round(((IHi-ILo)/(BPHi-BPLo))*(Cp-BPLo)+ILo)
    return Ip

report = open("AQIReport.txt","w")
for pm in PM10:
    Cp = pm['PM10']
    IHi, ILo, BPHi, BPLo = FindConstants(Cp)
    Ip = AQI(IHi, ILo, BPHi, BPLo, Cp)
    message = IndexMessage(Ip)
    print(f"PM10: {Cp}, AQI: {Ip}, Message: {message}")
    report.write(f"PM10: {Cp}, AQI: {Ip}, Message: {message}\n")

report.close()
    
