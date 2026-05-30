subjects = ["English","Hindi","Maths","Science","Arts"]
marks = {}
total = 0
for sub in subjects:
    while True:
        try:
            mark = int (input (f"Enter Mark of {sub} : "))
            if 0 <= mark <= 100:
                marks[sub] = mark
                total += mark
                break
            else:
                print("Marks must be between 0 and 100. Try again!")
        except ValueError :
            print("Invalid input! Please enter a number.")
avg= total/5  
perc = (total / 500) * 100
if 90 <= perc <= 100:
    grade = "A"
elif 80 <= perc <= 89:
    grade = "B"
elif 70 <= perc <= 79:
    grade = "C"
elif 60 <= perc <= 69:
    grade = "D"
else :
    grade = "F"

print("=" * 20, "Report Card" , "=" * 20)
for sub in marks:
    print(f"{sub} = {marks[sub]}")
print(f"Percentage : {perc}")
print(f"Grade : {grade}")
if perc >= 75:
    print( "Passed with Distinction ")