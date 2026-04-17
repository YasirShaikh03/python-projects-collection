import random
passowrd =" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]|\:;'<>,.?/"

lent_pass = int(input("Enter length of password : "))

a = "".join(random.sample(passowrd,lent_pass))
print(f"your paswood is {a}")


