marks = int(input("Enter your marks: "))

if 90 <= marks <= 100:
    print("Grade A")
elif 80 <= marks < 90:
    print("Grade B")
elif 70 <= marks < 80:
    print("Grade C")
else:
    print("Fail")