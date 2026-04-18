email=input("Enter Your Email ===]::::::::::::>  ").strip()

username= email[:email.index("@")]

domain = email[email.index("@")+1:]

formated=(f"Username is {username}\nDomain name is {domain_name}")

print(formated)