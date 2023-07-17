print("which operation would you like to perform")

print("ADDITON")

print("SUBSTRACTION")

print("MULTIPLICATION")

print("DIVISION")

print("MODULUS")

print("POWER OF FIRST NUMBER RAISED TO SECOND NUMBER")

n=int(input("enter the first number="))

m=int(input("enter the second number="))


print("press 1 for addition")
print("press 2 for substraction")
print("press 3 for multiplication")
print("press 4 for division")
print("press 5 for modulus")
print("press 6 for power")

a=int(input("enter the number="))

if(a==1):
  print(n+m)

if(a==2):
  print(n-m)

if(a==3):
  print(n*m)

if(a==4):
  print(n/m)

if(a==5):
  print(n%m)

if(a==6):
  print(n**m)

print("TASK COMPLETED SUCCESSFULLY")