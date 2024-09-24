#CaLara Boney
#9/24/2024
#P3HW1
#Module Average Calculator With Final Grade

#Allow user to input a grade for each module
a= float(input('Enter grade for Module 1: '))
b= float(input('Enter grade for Module 2: '))
c= float(input('Enter grade for Module 3: '))
d= float(input('Enter grade for Module 4: '))
e= float(input('Enter grade for Module 5: '))
f= float(input('Enter grade for Module 6: '))

#Calculate results
Sum_of_Grades =  a + b + c + d + e + f
avg = float(sum([a, b, c, d, e, f]) // 6)

#Show calculated results
print("\n------------Results------------")
print("Lowest Grade:", min([a, b, c, d, e, f]))
print("Highest Grade:", max([a, b, c, d, e, f]))
print("Sum of Grades:", Sum_of_Grades)
print("Average:", round(avg, 2))
print("\n------------------------------")

if avg >= 90:
    final_grade = "A"
elif avg >= 80:
    final_grade = "B"
elif avg >= 70:
    final_grade = "C"
elif avg >= 60:
    final_grade = "D"
elif avg >= 50:
    final_grade = "F"
    
print("Your grade is:", final_grade)
