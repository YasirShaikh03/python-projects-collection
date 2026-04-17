a=str(input("ENTER THE WHICH YOU WANT SHORT FORM  ::> " ))
text=a.split()
b=" "

for i in text:
    b = b + str(i[0]).upper()

print(b)