from datetime import datetime   
from playsound import playsoun

Alaram_Time = input("Enter a time of Alaram to be set:HH:MM:SS\n")
Alaram_Hours=Alaram_Time[0:2]
Alaram_MIN=Alaram_Time[3:5]
Alaram_SEC=Alaram_Time[6:8]
Alaram_Period=Alaram_Time[9:11].upper()
print("SETTTING UP ALARAM ......")
while True :
    now =datetime.now()
    curent_hour=now.strftime("%I")
    curent_MIN=now.strftime("%M")
    curent_SEC=now.strftime("%S")
    curent_PERIOD=now.strftime("%p")
    if(Alaram_Period==curent_PERIOD):
       if(Alaram_Hours==curent_hour):
         if(Alaram_MIN==curent_MIN):
            if(Alaram_SEC==curent_SEC):
                  print("Wake Up ")
                  playsoun("A:\for small phython project\mixkit-classic-alarm-995.wav")
                  break
      
   
   