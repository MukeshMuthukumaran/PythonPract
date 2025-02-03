

#main
f=0
password="2345"
for i in range(0,3):
    inp=input("Enter the password ")
    if(inp==password):
        f=1
        break

if(f==1):
    print("Acces Granted")
else:
    print("To Many Tryss")

