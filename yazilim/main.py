# -*- coding: utf-8 -*-
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from time import sleep
import ADS
from time import sleeptoken
import AHT10
cred = credentials.Certificate("login.json")
firebase_admin.initialize_app(cred)

ads = ADS.ADS1115() 
s1 = ads.readADCSingleEnded(channel=0)
s2 = ads.readADCSingleEnded(channel=1)
s3 = ads.readADCSingleEnded(channel=2)
s4 = ads.readADCSingleEnded(channel=3)

sens = AHT10.AHT10(1)
data = sens.getdata()
temp =data[0] 
hum = data[1]
Soil = {
    "Toprak1":s1,
    "Toprak2":s2,
    "Toprak3":s3,
    "Toprak4":s4,
}

Temp = {

    "Temp": temp,
    "Hum":hum,
}

res = db.collection("Raspberrypi").document("Toprak_Nem").update(Soil)
print("Toprak sensörü: {}".format(res)) 
res1 = db.collection("Raspberrypi").document("AHT-10").update(Temp)
print("Sıcaklık/nem sensörü: {}".format(res1)) 
