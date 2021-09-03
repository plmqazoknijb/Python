import math
import random
import datetime
# 1. 핸드폰 요금이 62421원 나왔다. 100원 미만은 절사한다고 한다. 62400원 청구. 59827원일 경우, 실제 청구 금액은?
print('--1번 문제--')
bill = 59827
bill2 = bill/100
bill3 = math.floor(bill2)*100
print(bill3)
# 2. 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다. 채점한 결과 93점이 나왔다. 90점 부여. 56점은 몇 점 부여?
print('--2번 문제--')
score = 56
print(round(score,-1))
# 3. 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
print('--3번 문제--')
for a in range(6):
    lotto = random.randrange(1,45)
    print(lotto)
# 4. 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)
print('--4번 문제--')
number = set()
while len(number)<3:
    number.add(random.randint(1,9))
print(number)
# 5. 내가 태어난 날로부터 며칠이 지났는지?
print('--5번 문제--')
now = datetime.datetime.now()
birthday = datetime.datetime(2004,7,2,9,23)
print(now-birthday)

# 6. 올해 크리스마스까지 며칠이 남았는지?
print('--6번 문제--')
christmas = datetime.datetime(2021,12,25,0,0)
print(christmas-now)

# 7. 내 생일이 며칠 남았는지?
print('--7번 문제--')
nextBirthday = datetime.datetime(2022,7,2,0,0)
print(nextBirthday-now)

# 8. 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?