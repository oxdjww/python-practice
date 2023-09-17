while True:
    print("[메뉴를 입력하세요]")
    print("1. 게임시작 2 랭킹보기 3. 게임종료")
    ipt = int(input())
    if ipt == 1:
        print("->게임을 시작합니다")
    elif ipt == 2:
        print("->랭킹보기")
    elif ipt == 3:
        print("게임을 종료합니다")
        break
    else:
        print("다시 입력하세요")