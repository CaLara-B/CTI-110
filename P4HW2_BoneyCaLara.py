# CaLara Boney
# 10/1/2024
# P3HW2
# Employee Database Loop

#Extra Variables Needed
employee_name = input("Enter employee's name: " )
all_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

#Employee Loop
while employee_name != "Done":
    all_employees += 1
    hours_worked = int(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    print("-----------------------------------")
    print("Employee name: \t", employee_name)
    print(f"{'Hours Worked':<18} {'Pay Rate':<18} {'Overtime':<18} {'Overtime Pay':<18} {'RegHour Pay':<18} {'Gross Pay':<18}")
    print("-----------------------------------------------------------------------------------------------------------")

    if hours_worked > 40:
        normal_pay = 40 * pay_rate
        overtime_pay = (hours_worked - 40) * (pay_rate * 1.5)
        overtime = hours_worked - 40
        gross_pay = normal_pay + overtime_pay
    else: 
        normal_pay = hours_worked * pay_rate
        overtime_pay = 0
        overtime = 0
        gross_pay = normal_pay + overtime_pay
    total_overtime_pay += overtime_pay
    total_regular_pay += normal_pay
    total_gross_pay +=  gross_pay
    print(f"{hours_worked:<18} ${pay_rate:<18.2f} {overtime:<18} ${overtime_pay:<18.2f} ${normal_pay:<18.2f} ${gross_pay:<18.2f}")
    employee_name = input("Enter employee's name: " )
    
#Bypassed loop totals
print()
print(f"Total number of employees entered: {all_employees} ")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f} ")
print(f"Total amount paid for regular hours: ${total_overtime_pay:.2f} ")
print(f"Total amount paid in gross: ${total_gross_pay:.2f} ")
