import random

lotto = []

def genLottoNum():
    return random.randint(1,45)

cnt = 0

while True:
    num = genLottoNum()
    if cnt > 5:
        break
    if num not in lotto:
        lotto.append(num)
        cnt += 1
        

print(lotto)
