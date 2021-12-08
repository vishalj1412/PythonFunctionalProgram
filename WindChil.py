import math
import sys


def windChill():
    
    t=float(sys.argv[1])
    v=float(sys.argv[2])
    if (3<=v<=120 and t <= 50):
        w = round((35.74 + 0.6215*t + (0.4275*t - 35.75)*math.pow(v, 0.16)), 2)  
        print("Wind Chill is :", w)
    else:
        print("enter temprature less than 50 and velocity is gretter than 3 and less than 120")


windChill()