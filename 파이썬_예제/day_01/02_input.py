name = input("이름을 입력하세요: ")
phone = input("번호를 입력하세요: ")
age = input("나이를 입력하세요: ")

print(name, phone, age)

print(name, "의 전화번호는", phone, "입니다.", "나이는", age)
print("내 이름은 {}이고 나이는 {}살입니다.".format(name, age))
print(f"내 이름은 {name}이고 나이는 {age}살입니다.")

print(type(name))
print(type(age))