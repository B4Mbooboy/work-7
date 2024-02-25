score = int(input("กรุณาใส่คะแนนของคุณ: "))
if score >= 80:
    grade = "A"
elif 70 <= score <= 79:
    grade = "B"
elif 60 <= score <= 69:
    grade = "C"
elif 50 <= score <= 59:
    grade = "D"
else:
    grade = "F"
print(f"คุณได้เกรด: {grade}")
