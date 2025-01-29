#main

name=input("Enter name ")
number=int(input("Enter number "))
month="January 2025"
amt=1;
add=input("Enter the address")
unit=int(input("Enter the total number of unit consumed"))
if unit<=50:
    amt=unit*30
elif unit >=51 and unit<=100:
        amt=unit*35
elif unit >=101 and unit<=150:
            amt=unit*40
elif unit>150:
                amt=unit*50
else:
                    print("enter the correct unit in numbers")

print(amt)

print("TAMIL NADU ELECTRICITY BOARD (TNEB)  \n------------------------------------------------")
print("Biling Month:            :",month)
print("Consumer No:             :",number)
print("Consumer Name:           :",name)
print("Address:                 :",add)
print("Unit Consumed:             :",unit)
print("------------------------------------------------")
print("Total Amount (INR):             :",amt)


print("------------------------------------------------")




