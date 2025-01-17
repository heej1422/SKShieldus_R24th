# 총 5명의 학생의 성적을 입력 받는다
# 최대 점수, 최소 점수, 성적 평균을 구한다
# 80점 이상의 학생 수를 카운트 한다

STUDENTS = 5
scores = []
count = 0

for i in range(STUDENTS):
    score = int(input(f"{i+1}번째 학생의 성적을 입력하세요: "))
    scores.append(score)

    if score >= 80:
        count += 1

print(f"최대 점수는 {max(scores)}이고, 최소 점수는 {min(scores)}이고, 평균 점수는 {sum(scores)/STUDENTS}입니다.")
print(f"80점 이상 받은 학생은 총 {count}명입니다.")


