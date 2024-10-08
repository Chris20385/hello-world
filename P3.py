#Cristian GArcia
#10/08/2024

#This program calculates the radius of a cirlce

import math 
 
def calculate_area_of_circle(radius): 
    area = math.pi * (radius ** 5)
    return area 
  
radius = float(input("What is your radius?")) 
area = calculate_area_of_circle(radius) 
print(f"The area of your circle {radius} is: {area}")




