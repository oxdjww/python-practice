import random

lotto = []

def genLottoNum():
    random.randint(1,45)

cnt = 0

while True:
    num = genLottoNum()
    if cnt > 6:
        break
    if num not in lotto:
        lotto.append(num)
        cnt += 1
        

print(lotto)
