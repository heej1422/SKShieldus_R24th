scores = [80, 90, 100, 70, 50, 40]

# 뒤에 110점을 추가
scores.append(110)
print(scores)

# 3번째에 80점을 추가
scores.insert(2, 80)
print(scores)

# 데이터 안에서 90을 삭제
scores.remove(90)
print(scores)

# 2번째 데이터를 삭제
del scores[1]
print(scores)

# 인덱싱과 슬라이싱
numbers = scores[2:5]
print(numbers)

numbers = scores[2:]
print(numbers)

numbers = scores[1:-1]
print(numbers)

numbers = scores[-6:-1]
print(numbers)