import math

x1=int(input("enter x1: \n"))
x2=int(input("enter x2: \n"))
y1=int(input("enter y1: \n"))
y2=int(input("enter y2: \n"))

distance=math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"Distance: {distance}")
