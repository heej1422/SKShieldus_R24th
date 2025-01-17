names = ['홍길동', '심청이', '이몽룡']

print(names)
print(['홍길동', '심청이', '이몽룡'])

print(names[0])
print(print(['홍길동', '심청이', '이몽룡'][0]))

for name in names:
    print(name)

for i in range(len(names)):
    print(f"{i+1}번째 : {names[i]}")

for i, name in enumerate(names):
    print(f"{i+1}번째: {name}")
