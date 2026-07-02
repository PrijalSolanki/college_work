product=['abc','kbc','xyz',' ',' ','def','ghi','jkl']
print(product)
s=input("Search Data: ")
if s in product:
    print("Avaiable product !!")
else:
    print("Avaiable Not product !!")
ui=int(input("Enter index which index u want to update: "))
p=input("Update product: ")
product[ui]=p
print(product)
if " " in product:
    print("slot Available !!")
else:
    print("Slot cannt Available !!")
print(product)