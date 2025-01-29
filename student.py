#mian
name=input("Enter Name ")
num=input("Enter RollNumber ")
cls=input("Enter Class / Section ")
m1=int(input("Enter mark 1 "))
m2=int(input("Enter mark 2 "))
m3=int(input("Enter mark 3 "))
m4=int(input("Enter mark 4 "))
m5=int(input("Enter mark 5 "))
tot=m1+m2+m3+m4+m5
per=(tot/500)*100


if per>100:
    print("enter in the limit the limit is exeed ")
elif per>91:
    grade="A+"
elif per>=80 and per<=89:
    grade="A"
elif per>=70 and per<=79:
    grade="B+"
elif per>=60 and per<=69:
    grade="B" 
elif per>=50 and per<=59:
    grade="C"
else:
    grade="F"
    



print("STUDENT GRADE REPORT \n ------------------------------")
print("Student Name         : ", name)
print("Roll Number          :", num)
print("Class/Section        :", cls)
print("------------------------------")
print("Subject 1            :", m1)
print("Subject 2            :", m2)
print("Subject 3            :",m3)
print("Subject 4            :",m4)
print("Subject 5            :",m5)
print("------------------------------")
print("Total Markds         :",tot)
print("Percentage           :",per)
print("Final Grade          :",grade)
if grade=="F":
   res="FAIL"
else:
   res="PASS"

print("RESULT               :",res)
print("------------------------------")
    


