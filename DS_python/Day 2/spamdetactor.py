blacklist_mail=["jay@gmail.com","raj@gmail.com","roshan@gmail.com","ur@gmail.com"]
print(blacklist_mail)
mail=input("Enter your email: ")
if mail in blacklist_mail:
    print("This is a blacklisted email")
else:
    print("You are welcome to our website")