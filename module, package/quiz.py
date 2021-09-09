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
#다른 방법
print(round(score/10)*10)
# 3. 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
print('--3번 문제--')
for a in range(6):
    lotto = random.randrange(1,45)
    print(lotto)
#다른 방법
random.sample(range(1,46),6)
# 4. 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)
print('--4번 문제--')
number = set()
while len(number)<3:
    number.add(random.randint(1,9))
print(number)
#다른방법
list_r = random.sample(range(1,10),3)
print("".join(str(n)for n in list_r))
print("".join(map(str,list_r)))
# map()은 하나씩 꺼내서 적용한다.
# 5. 내가 태어난 날로부터 며칠이 지났는지?
print('--5번 문제--')
now = datetime.datetime.now()
birthday = datetime.datetime(2004,7,2,9,23)
#엄마
mbirthday = datetime.datetime(1970,5,30,0,0)
print(now-birthday)
print(now-mbirthday)

# 6. 올해 크리스마스까지 며칠이 남았는지?
print('--6번 문제--')
christmas = datetime.datetime(2021,12,25,0,0)
print(christmas-now)

# 7. 내 생일이 며칠 남았는지?
print('--7번 문제--')
nextBirthday = datetime.datetime(2022,7,2,0,0)
print(nextBirthday-now)
# 다른 방법
nextBirthday2 = datetime.datetime(2020,7,3,0,0)
if nextBirthday2 < now:
    nextBirthday2 = nextBirthday2.replace(year=nextBirthday2.year + 1)
print(nextBirthday2 - now)

# 8. 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?
# 마지막 번호가 몇 번인지 묻자
last_number = input("마지막 번호는? ")
#1부터 마지막 번호까지 리스트 만들자
list_class = list(range(1,int(last_number)+1))

# 무한 반복
while True:
# 나간 친구의 번호 묻자
    exclude_number = input("뺄 번호는?(그냥 enter치면 끝내자)")
# 그냥 enter면 반복 끝내자
    if exclude_number =='':
        break
# 리스트에서 빼자
    list_class.remove(int(exclude_number))
    print(list_class)
#랜덤으로 섞자
random.shuffle(list_class)
#출력하자
#print(list_class)
print('자리\t학생번호')
for index, n in enumerate(list_class):
    print(f'{index+1}\t{n}')

