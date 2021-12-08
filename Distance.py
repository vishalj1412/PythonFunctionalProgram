import sys
import math

x=int(sys.argv[1])
y=int(sys.argv[2])

distance=math.pow((x*x+y*y),1/2)
print("distance of (x,y) point to origin is :",distance)