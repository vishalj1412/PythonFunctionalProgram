import math
a=int(input("enter value of a : "))
b=int(input("enter value of b : "))
c=int(input("enter value of c : "))
delta=abs(b*b-4*a*c)
root1=(-b+math.sqrt(delta))/(2*a)
root2=(-b-math.sqrt(delta))/(2*a)

print("roo1 : ",root1)
print("root2 : ",root2)
