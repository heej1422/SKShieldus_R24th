from faker import Faker

fake = Faker('ko_KR')

names = []
phone_numbers = []
addresses = []

for i in range(10):
    name = fake.name()
    phone_number = fake.phone_number
    address = fake.address

    names.append(name)
    phone_numbers.append(phone_number)
    addresses.append(address)

for i in range(10):
    print(f"이름: {names[i]}, 전화번호: {phone_numbers[i]}, 주소: {addresses[i]}")
    
