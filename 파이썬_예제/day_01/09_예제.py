# while 반복
# 메뉴를 선택한다. (여러 개의 메뉴 선택)
# 구매한 메뉴를 리스트로 보관
# 현금 입력
# 거스름돈 계산
# 구매했던 리스트와 총 구매가격

menus = {"아메리카노":4000, "카페라떼":5000, "카페모카":6000}
order_list = []
total_price = 0

print("*"*50)
print("======== 메뉴 ========")

for name, price in menus.items():
    print(f"{name}: {price}원")

print("*"*50)

while True:
    selected_menu = input("▶ 주문할 메뉴를 입력하세요(*주문종료=q): ")
    price = menus.get(selected_menu, 0)

    if price != 0:
        order_list.append(selected_menu)
        total_price = total_price + price

    elif selected_menu == "q":
        print("\n▶ 주문 종료합니다 ◀")
        break
    else:
        print("\n▶ 해당 메뉴가 없습니다. 다시 입력하세요 ◀")

print("*"*50)

if len(order_list) == 0:
    print("\n▶ 주문한 메뉴가 없습니다. ◀")

else:
    money = int(input("\n▶ 지불할 금액을 입력하세요: "))

    change = money - total_price

    if change >= 0:
        print(f"\n▶ {order_list} 구매 완료. 거스름 돈은 {change}원 입니다.")
    else:
        print(f"\n▶ {order_list} 구매 실패. 돈이 부족합니다.")

print("*"*50)