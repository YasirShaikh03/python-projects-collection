Height = float(input("Enter Your Height (in meter)  :"))
Weight= float(input("Enter Your Weght (in kg) :"))
BMI= Weight/(Height*Height)

if(BMI < 18.5):
    print(f"UnderWeight {BMI}")
elif(BMI > 18.5 and  BMI < 24.9):
    print(f"Normal weight {BMI}")
elif(BMI > 25.0 and BMI < 29.9):
    print(f"Overweight  {BMI} ")
    
else:
    print(f"Obesity  {BMI}")