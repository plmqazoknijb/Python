from baseball_game_engine import make_quiz, check

answer = make_quiz()
#print(answer)
# 무한반복
while True:
# 숫자 3자리 중북없이 묻자
    player = input("숫자 세자리는? ")
    try:    #숫자가 아닐 때 에러 처리
        palyer_int = int(player)
    except ValueError:
        continue
    #길이가 3이 아닐 때 에러 처리
    if len(player) != len(answer):
        #raise InvalidCountError("3자리가 아닙니다.")
        print(f'입력한 숫자의 개수가 정답과 다릅니다.정답: {len(answer)}')
        continue
# strike, ball 확인하자
    strike, ball = check(answer,player)
# 출력하자
    print(f'{player}\tstrike: {strike}\tball: {ball}')
# strike가 3일때, 반복문 끝내기
    if strike ==3:
        break
#축하해주자
print('축하합니다. 짝짝짝👏👏')