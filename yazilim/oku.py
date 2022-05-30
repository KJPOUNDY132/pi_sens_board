# -*- coding: utf-8 -*-
import ADS
from time import sleeptoken
ads = ADS.ADS1115() 

# mqtt bağlantı mesaj paylaşma fonksyonları
"""#################################################################### """ 
volt1 = ads.readADCSingleEnded(channel=0)

    