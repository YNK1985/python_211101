# ifelse.py

score = int(input("enter your score:"))

if 90 <= score <= 100:
    grade = "A"
elif 80 <=score < 90:
    grade = "B"
elif 70 <=score < 800:
    grade = "C"
else:
    grade = "D"

print ("Your grade is",grade,".")
