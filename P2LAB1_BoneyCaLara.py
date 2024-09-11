# CaLara Boney
# 9/11/2024
# P2LAB1
# Calculate math related to a circle

# Import the math library
import math

# Get float input from user (radius)
radius = float(input("What is the radius of the circle? "))
print()

#Calculate diameter
diameter = radius * 2
print("The diameter of the circle is", round(diameter, 1))
print()

#Calculate circumference
circumference = 2 * math.pi * radius
print("The circumference  of the circle is", round(circumference, 2))
print()

#Calculate the area
area = math.pi * (radius **2)
print("The radius of the circle is", round(area, 3))
print()
