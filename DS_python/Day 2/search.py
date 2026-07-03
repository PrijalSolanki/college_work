std=["jay","ray","voy","joy","roy"]
print(std)
sr=input("Enter the name to search: ")
if sr in std:
    print(f"{sr} is Present.")
else:
    print(f"{sr} is Not Present.")