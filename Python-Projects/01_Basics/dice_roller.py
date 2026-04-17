import random

min_Value=1
max_Value = 6

roll_Agian = str(input("Enter if you want dice TYPE YES | Y  IF you DONT THEN NO OR N   : ")).upper()

if roll_Agian == "YES" or roll_Agian == "Y":
     print(random.randint(min_Value, max_Value))
elif(roll_Agian=="NO" or roll_Agian == "N"):
    print("OK! THANKS, PLAY AGAIN IF YOU WANT")
    
               
            
else:
     print("INVALID INPUT")
           
        
       
       