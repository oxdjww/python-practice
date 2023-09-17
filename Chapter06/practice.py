# price = int(input("삼성전자 주식 가격 : "))
# if price>=90000:
#     print("매도합니다")
# elif price>=80000:
#     print("대기중입니다")
# else:
#     print("매수합니다")

bag_price = float(input("가방금액 : "))
watch_price = float(input("시계금액 : "))
total_price = bag_price+watch_price
if total_price>=100000:
    rate = 0.3
elif total_price>=50000:
    rate = 0.2
else:
    rate = 0.1
print("결제금액 : " + str(total_price * (1-rate)))