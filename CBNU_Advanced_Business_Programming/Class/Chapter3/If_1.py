value = 10
if value > 5:
    print("Value is Bigger Than 5")

score = int(input(('Input Score : ')))      # 사용자로부터 정수값을 입력 받습니다.

if 90 <= score <= 100:
    grade = "A"

elif 80 <= score < 90:
    grade = "B"

elif 70 <= score < 80:
    grade = 'C'

elif 60 <= score < 70:
    grade = 'D'

else:
    grade = 'F'

print("Grade is " + grade)