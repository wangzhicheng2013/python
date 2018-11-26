import sys
score = int(raw_input("score = "))
if score < 0 or score > 100:
    raise TypeError("invalid score...!")
if score >= 90:
    grade = "A"
elif score <= 89 and score >=60:
    grade = "B"
else:
    grade = "C"
print grade

            
