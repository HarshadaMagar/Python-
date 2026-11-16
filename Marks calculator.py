name = input("Enter student name: ")

m1 = float(input("Enter marks in Python: "))
m2 = float(input("Enter marks in Mathematics: "))
m3 = float(input("Enter marks in Statistics: "))

total = m1 + m2 + m3
percentage = total / 3

print("\nStudent Result")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")

if percentage >= 75:
    print("Grade: Distinction")
elif percentage >= 60:
    print("Grade: First Class")
elif percentage >= 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")
