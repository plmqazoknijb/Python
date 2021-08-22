#숫자  자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

#문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

#boolean 자료형
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))

#변수
#1.애완동물 소개
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby = "공놀이"
print(name, "는",  age, "살이며, ", hobby, "을 아주 좋아해요")
#(+)말고 콤마도 사용가능하고 콤마 사용 시 정수형이나 boolean변수를 그대로 사용가능 / 콤마는 빈칸 하나 생김
print(name + "는 어른일까요?" + str(is_adult))

#주석
#한줄 주석
'''
여러문장 주석'''
#(ctrl + /) 는 주석처리, 해제시 한번 더

#Quiz 1
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

#연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)
print(2**3) #2^3

print(5%3)
print(10%3)
print(5//3)
print(10//3) #나머지가 있는 나눗셈의 몫 출력

print(10>3)
print(4>=7)
print(10<3)
print(5<=5)

print(3==3)
print(4==2)
print(3+4==7)

print (1!=3)
print(not(1!=3))

print((3>0) and (3<5))
print ((3>0) & (3<5))
print((3>0) or(3>5))
print((3>0) | (3>5))
print(5>4>3)
print(5>4>7)

#간단한 수식
print(2+3*4)
print((2+3)*4)
number = 2+3*4
print(number)
number= number+2
print(number)
number += 2
print(number)
number *=2
print(number)
number /= 2
print(number)
number -=2
print(number)
number%=5
print(number)

#숫자 처리 함수(36:26)
print(abs(-5)) #절댓값
print(pow(4,2)) #4^2
print(max(5,12))#최댓값
print(min(5,12))#최소값
print(round(3.14))#반올림
print(round(4.99))

from math import *
print(floor(4.99)) #내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) #제곱근 (4)

#랜덤함수
from random import *

print(random()) #0.0 ~ 1.0미만의 임의의 값 생성
print(random()*10) #0.0~10.0 미만의 임의의 값 생성
print(int(random()*10)) #0~10 미만의 임의 값 생성
print(int(random()*10))
print(int(random()*10))
print(int(random()*10)+1)#1~10이하의 값 생성
print(int(random()*10)+1)
print(int(random()*10)+1)
print(int(random()*45)+1) #1~45 이하의 값 생성
print(randrange(1,46))#1~46 미만의 임의의 값 생성
print(randint(1,45)) #1~45 이하의 임의의 값 생성

#Qiuz 2
from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " +str(date) +"일로 선정 되었습니다.")

#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3="""
나는 소년이고,
파이썬은 쉬워요"""
print(sentence3)

#슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) #0부터 2직전 까지(0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])#처음부터 6직전까지
print("뒤 7자기 : " + jumin[7:])#7부터 끝까지
print("뒤 7자리(뒤에부터) : " + jumin[-7:])#맨 뒤에서 7번째 끝까지

#문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("Java"))
#print(python.index("Java"))

print(python.count('n'))

#문자열 포멧
#방법1
# print("나는 %d살입니다." %20)
# print("나는 %s을 좋아해요." %"파이썬")
# print("Apple은 %c로 시작해요" %"A")
# print("나는 %s살입니다." %20)
# print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

#방법2
# print("나는 {}살입니다".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

#방법3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간",age = 20))

#방법4
age = 20
color="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요." )

#탈출문자

# print("백문이 불여일견\n백견이 불여일타")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다")
# print("저는 \'나도코딩\'입니다")
#\\ : 문장내에서 \

#\r :커서를 맨 앞으로 이동
# print("Red Apple\rPine")

#\b :백스페이스
#print("Redd\bApple")

#\t : 탭
print("Red\tApple")

#Quiz 3
url = "http://naver.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
pw = my_str[:3]+str(len(my_str)) +str(my_str.count("e"))+"!"
print("{0}의 비밀번호는 {1}입니다.".format(url,pw))

#리스트
#순서를 가지는 객체의 집합
subway=[10,20,30]
print(subway)

subway=["유재석","조세호","박명수"]
print(subway)

#조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

#하하씨가 다음 정류정에서 다음 칸에 탐
subway.append("하하")#맨뒤에 추가
print(subway)

#정형돈씨를 유재석/조세호 사이에 태움
subway.insert(1,"정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
num_list2 = [5,2,4,3,1]
mix_list = ["조세호",20,True]

#리스트 확장
num_list2.extend(mix_list)
print(num_list2)

#사전
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
# # print(cabinet[5]) --> 오류
#
# print(cabinet.get(3))
# # print(cabinet.get(5))-->None출력
# print(cabinet.get(5,"사용 가능"))
#
# print(3 in cabinet)
# print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["c-20"]="조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#key들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 페점 (아무도 없게)
cabinet.clear()
print(cabinet)

#튜플
#값을 고정해서 사용, 수정 불가능
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
(name, age, hobby)=("김종국",20,"코딩")
print(name, age, hobby)

#세트(집합)
#중복 안됨, 순서 없음
my_set ={1,2,3,3,3}
print(my_set)

java ={"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

#교집합 (둘다)
print(java & python)
print(java.intersection(python))

#합집합(둘중에 하나)
print(java | python)
print(java.union(python))

#차집합(자바만)
print(java-python)
print(java.difference(python))

#파이썬 할 줄 아는 사람 늘어남
python.add("김태호")
print(python)

#자바를 못하게 됨
java.remove("김태호")
print(java)

#자료구조의 변경
menu = {"커피","우유","주스"}
print(menu,type(menu))

menu = list(menu)
print(menu,type(menu))

menu = tuple(menu)
print(menu,type(menu))

menu = set(menu)
print(menu,type(menu))

#Quiz4
from random import  *
users = range(1,21)
users = list(users)
winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다. --")

#if
# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")
#
# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp <30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 날씨에요")
# else:
#     print("너무 추워요. 나가지 마세요")

#for
for watting_no in range(5):
    print("대기번호 : {0}".format(watting_no))

#while
customer = "토르"
index = 5
# while index >= 5:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unkown"
#
# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

#continue와 break
absent =[2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

#한줄 for문
# students = [1,2,3,4,5]
# print(student)
# students = [i+100 for i in students]
# print(students)
#
# students = ["Iron man", "Thor", "I an groot"]
# students = [len(i) for i in students]
# print(students)

students = ["Iron man", "Thor", "I an groot"]
students = [i.upper() for i in students]
print(students)

#Quiz 5
from random import *
cnt = 0
for i in range(1,51): # 승객
    time = randrange(5,51) # 5~50분 소요 시간
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt += 1
    else:
        print("[ ] {0}번쨰 손님 (소요시간 : {1}분)".format(i,time))

print(("총 탑승 승객 : {0} 분".format(cnt)))

#함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

#전달값과 반환값
def deposit(balance, money):
    print("입금이 완려되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance
def withdraw_night(balance, money):
    commission = 100
    return commission, balance-money-commission
balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance,500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission,balance))

#기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))
#
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이: {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
#
# profile("유재석")
# profile("김태호")

#키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

#가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t".format(name, age),end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이: {1}\t".format(name, age),end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "","","")

#지역변수와 전역변수
gun =10

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def chckpoint_ret(gun, soldiers):
    gun = gun- soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = chckpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))

def std_weight(height, gender):
    if gender =="남자":
        return height * height *22
    else:
        return height * height *21

height =175
gender = "남자"
weight = round(std_weight(height/100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

#클래스
# #마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린"
# hp = 40
# damage = 5
#
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0},공격력 {1}\n".format(hp,damage))
#
# #탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반모드 / 시즈모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
#
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0},공격력 {1}\n".format(tank_hp,tank_damage))
#
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35
#
# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0},공격력 {1}\n".format(tank2_hp,tank2_damage))
#
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location , damage))
#
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

class Unit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage = damage
        print("{0}유닛이 생성 되었습니다.".format(self.name))
        print("체력{0}, 공격력{1}".format(self.hp,self.damage))

marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank = Unit("탱크", 150,35)

#__init__ (생성자)
# marine2 = Unit("마린") 매개변수를 개수만큼 주어야 함

#멤버변수
wraith1 = Unit("레이스",80,5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))

wraith2 = Unit("레이스",80,5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

#메소드
class AttackUnit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self,location):
        print("{0}:{1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name,location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

#상속
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

#다중 상속
# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

#메소드 오버라이딩
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시") # 오버라이딩된 move() 호출

#pass
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") # 체력 500, 생성 위치 7시

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

#super
class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


# class FlyableUnit(Unit, Flyable):
class FlyableUnit(Flyable, Unit):  # 순서 변경
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)  # Unit 클래스 생성자 호출
        Flyable.__init__(self)  # Flyable 클래스 생성자 호출

dropship = FlyableUnit()

#스타크래프트 프로젝트 전반전
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))  # 출력문 추가

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
              .format(self.name, location, self.speed))

    def damaged(self, damage):  # AttackUnit 에서 Unit 으로 이동
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
              .format(self.name, location, self.damage))


# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)  # 이름, 체력, 이동속도, 공격력

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))


# 탱크
class Tank(AttackUnit):
    siege_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.siege_mode = False  # 시즈모드 (해제 상태)

    # 시즈모드
    def set_siege_mode(self):
        if Tank.siege_developed == False:  # 시즈모드가 개발되지 않은 경우 메소드 탈출
            return

        # 현재 시즈모드가 아닐 때
        if self.siege_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.siege_mode = True
        # 현재 시즈모드일 때
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.siege_mode = False


# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)


# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.cloaked = False

    # 클로킹 모드
    def cloaking(self):
        if self.cloaked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.cloaked = False
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.cloaked = True

#스타크래프트 프로젝트 후반전
# 게임 시작
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

# 게임 종료
def game_over():
    print("Player : gg") # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 실제 게임 진행
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t1)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.siege_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): # Marine 의 인스턴스이면 스팀팩
        unit.stimpack()
    elif isinstance(unit, Tank): # Tank 의 인스턴스이면 시즈모드
        unit.set_siege_mode()
    elif isinstance(unit, Wraith): # Wraith 의 인스턴스이면 클로킹
        unit.cloaking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 (5 ~ 20)

# 게임 종료
game_over()

#Quiz 8
class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type,
        self.price, self.completion_year)


houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()

