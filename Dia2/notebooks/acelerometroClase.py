import android
import time
import csv

dt = 100
fin = 5000
tiempo = 0

droide = android.Android()
droide.startSensingTimed(2,dt)
lecturas = []
while tiempo <= fin:
    lecturas.append(droide.sensorsReadAccelerometer().result)
    time.sleep(dt/1000.0)
    tiempo += dt
droide.stopSensing();

with open ('test.csv','w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(lecturas)