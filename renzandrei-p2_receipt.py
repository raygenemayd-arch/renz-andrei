def compute_average(s1, s2, s3):
    return (s1 + s2 + s3) / 3

s = int(input("How many students? "))

if s < 3:
    s = 3

for i in range(1, s+1):
    print("\nStudent", i)
    name = input("Enter name: ")
    a1 = float(input("p 1: "))
    a2 = float(input("p 2: "))
    a3 = float(input("p 3: "))

    average = compute_average(a1, a2, a3)

    if average >= 90 and average <= 100:
        status = "Excellent"
    elif average >= 80 and average <= 89:
        status = "Very Good"
    elif average >= 75 and average <= 79:
        status = "Passed"
    else:
        status = "Failed"

    print("Average:", average)
    print("Status:", status)
