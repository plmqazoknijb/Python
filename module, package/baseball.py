from baseball_game_engine import make_quiz, check

answer = make_quiz()
print(answer)
# 무한반복
while True:
# 숫자 3자리 중북없이 묻자
    player = input("숫자 세자리는? ")
# strike, ball 확인하자
    strike, ball = check(answer,player)
# 출력하자
    print(f'{player}\tstrike: {strike}\tball: {ball}')
# strike가 3일때, 반복문 끝내기
    if strike ==3:
        break
#축하해주자
print('축하합니다. 짝짝짝👏👏')