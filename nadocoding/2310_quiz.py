#퀴즈 1-1
id_number ="040702"
print(id_number[:2]+"\n"+id_number[2:])
print(int(id_number[:2])*int(id_number[2:]))

#퀴즈 1-2
phone_number = "02-1234-5678"
print(phone_number[:phone_number.index("-")])
print(phone_number[-4:])

#전화번호 입력시, -가 있든, -가 없든 찰떡같이 알아먹기
phone_number1 = "010-1234-5678"
phone_number2="01011112222"
phone_number3="010 3333 4444"

result = phone_number1.replace('-','').replace(' ','')
print(result)

#퀴즈 2-1
# student_number = "2313"
# if student_number[1] == 1 or student_number[1] == 2:
#     print(student_number[1] + "반 뉴미디소프트웨어과")
# elif student_number[1] == 3 or 4:
#     print(student_number[1] + "반 뉴미디어웹솔루션과")
# elif student_number[1] == 5 or 6:
#     print(student_number[1] + "반 뉴미디어디자인과")
# else:
#     print("잘못 입력했습니다")

# student_number = "2313"
# number = student_number.index()
# major = ['뉴미디어소프트웨어과','뉴미디어소프트웨어과','뉴미디어웹솔루션과','누미디어웹솔루션과','뉴미디어디자인과','뉴미디어디자인과' ]
# print(f'{number}반 {major[number-1]}')

student_number = "2313"
number = student_number[1]
number = int(number)
majors = ['뉴미디어소프트웨어과','뉴미디어웹솔루션과','뉴미디어디자인과']
if 1<= number <=6:
    print(f'{number}반 {majors[(number-1) // 2]}')
else:
    print("잘못 입력했습니다")


#퀴즈 2-2
def get_major(student_number):
    major = "잘못입력했습니다"
    grade = student_number[0]
    if student_number[1] =="1" or student_number[1] =="2":
        major = "뉴미디어소프트웨어과"
    elif student_number[1] == "3" or student_number[1]=="4":
        major = "뉴미디어웹솔루션과"
    elif student_number[1] == "5" or student_number[1]=="6":
        major = "뉴미디어디자인과"
    return grade, major
grade,major = get_major("2310")
print(major,grade)

#퀴즈 2-3
def average(*number):
    sum = 0
    for num in number:
        sum+=num
    return sum / len(number)

print(average(10,20,30))

#퀴즈 2-4
def get_bmi(height, weight):
    bmi = round(weight/((height/100)*(height/100)),1)
    if bmi < 18.5:
        result = "저체중"
    elif 18.5 <= bmi <23:
        result = "보통"
    elif 23 <= bmi <25:
        result = "과체중"
    else:
        result = "비만"
    return result
bmi = get_bmi(176, 69)
print(bmi)

# 구구단 7단 출력하기
for i in range(1, 9 + 1):  # i : 1~9
    print(f'7 x {i} = {7 * i}')
# 구구단 2~9단 출력하기
for dan in range(2, 10):  # dan: 2~9
    for i in range(1, 9 + 1):  # i : 1~9
        print(f'{dan} x {i} = {dan * i}')
    print('-' * 10)
# 구구단 2~7단까지 출력하기
for dan in range(2, 9 + 1):  # dan: 2~9
    for i in range(1, 9 + 1):  # i : 1~9
        print(f'{dan} x {i} = {dan * i}')
    print('-' * 10)
    if dan == 7:
        break
# 구구단 2~7단 출력하되, x1, x3, x5, x7, x9 인 것만 출력하기
for dan in range(2, 9 + 1):  # dan: 2~9
    for i in range(1, 9 + 1):  # i : 1~9
        if i % 2 == 0:  # i == 2 or i == 4 or i == 6 or i == 8:
            continue
        print(f'{dan} x {i} = {dan * i}')
    print('-' * 10)
    if dan == 7:
        break

#quiz 3-1
def n_sum(argument):
    sum = 0
    number=str(argument)
    if len(number)<10:
        # for a in range(0,len(number)):      #range(3): a: 0 1 2
        #     sum+=int(number[a])
        for a in number:        #for a in '408':  a:'4'
            sum += int(a)
        return sum
    else:
        return -1

result = n_sum(10)
print(result)        #1
result = n_sum(331)
print(result)         #7
result = n_sum(408)
print(result)         #12
result = n_sum(1000000000)
print(result)         #-1

#quiz 3-2
def get_subway_fare(km):
    if km<11:
        fare = 720
        return fare
    elif km<50:
        bonus = km-10
        more =bonus%5
        if more!=0:
            more=100
        fare = 720+((bonus//5)*100)+more
        return fare
    else:
        bonus = km - 50
        more = bonus % 8
        if more!=0:
            more=100
        fare = 720 + ((50-10)//5)*100 + ((bonus // 8) * 100) + more
        return fare
fare = get_subway_fare(5)
print(fare)        #720
fare = get_subway_fare(26)
print(fare)        #1120
fare = get_subway_fare(27)
print(fare)        #1120
fare = get_subway_fare(58)
print(fare)        #1620
fare = get_subway_fare(59)
print(fare)        #1720
fare = get_subway_fare(61)
print(fare)        #1720

#quiz3-3
def get_three_six_nine(num):
    number=str(num)
    a = number.count("3")+number.count("6")+number.count("9")
    if a>=1:
        return "짝"*a
    else:
        return number
result = get_three_six_nine(1)
print(result)        #1
result = get_three_six_nine(3)
print(result)        #짝
result = get_three_six_nine(16)
print(result)        #짝
result = get_three_six_nine(36)
print(result)        #짝짝

#quiz 3-4
"""사용자 2명으로부터 가위, 바위, 보를 입력 받아 함수를 만들어서 "비겼습니다" "바위 승!" "가위 승!" "보 승!"과 같이 승패를 결정하는 프로그램 만들어보자
1.get_rock_paper_scissors 함수를 만든다.
2. 인수를 String으로 총 2개를 넣는다.
3. 승패에 대한 답변을 return 한다.
4.result = get_rock_paper_scissors(p1, p2)
  print(result)
"""


p1, p2 = input("가위, 바위, 보 중 선택 : "), input("가위, 바위, 보 중 선택 : ")
list = ["가위", "바위", "보"]
def get_rock_paper_scissors(a, b):
    if (a == b):
        return("비겼습니다!")
    elif (a == list[0] and b == list[1]) or (b == list[0] and a == list[1]):
        return("바위가 이겼습니다!")
    elif (a == list[0] and b == list[2]) or (b == list[0] and a == list[2]):
        return("가위가 이겼습니다!")
    elif (a == list[1] and b == list[2]) or (b == list[1] and a == list[2]):
        return("보가 이겼습니다!")
result = get_rock_paper_scissors(p1, p2)
print(result)


# Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
# is_prime() 함수를 만든다.
# 인수로 1개의 숫자를 받는다.
# 인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.

def is_prime(number):
  for i in range(2,number-1):
      result = number%i
      if result == 0:
            return "소수가 아닙니다."
  else:
      return "소수 입니다."
result = is_prime(36)
print(result)
result = is_prime(13)
print(result)
result = is_prime(2)
print(result)

# Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다.
# 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
# '고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
# '놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다.
# '''
# result = get_compliment('고구마 된장국')
# print(result) # 왓쇼이!
# result = get_compliment('맛있는 크레이프')
# print(result) # 우마이!
# result = get_compliment('놀랄 만한 상황')
# print(result) # 요모야..!
# result = get_compliment('좋은 마음가짐이다!')
# print(result) # 으무!

def get_compliment(text_str):
    if text_str.count("고구마"):
        return "왓쇼이!"
    elif text_str.count("맛있는"):
        return "우마이!"
    elif text_str.count("놀랄 만한"):
        return "오모야!"
    else:
        return "으무!"
result = get_compliment("고구마 된장국")
print(result)
result = get_compliment("맛있는 크레이프")
print(result)
result = get_compliment("놀랄 만한 상황")
print(result)
result = get_compliment("좋은 마음가짐이다!")
print(result)

#퀴즈 5-1 ~ 5-5.
    #1.모듈이란 - 비슷한 성실끼리의 함수나 변수 또는 클래스를 모아 놓은 파일이다.
    #2.패키지란 - 모듈들을 모아둔 집합
    #3.theater_module의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성
from theater_module import price as p2310
#p2310(2)
    #4.__all__의 역할 - 실제 패키지를 만든 사람은 공개범위를 설정해 줄 수 있다.
    # 이때 __all__이라는 변수에 리스트 형태로 공개하려는 모듈 이름을 추가하면 해당모듈에 대해 공개 설정을 할 수 있게 된다.
    #5. if __name__ == "__main__":
    #       trip_to = ThailandPackage()
    #       trip_to.detail()
    #   else:
    #6. <가> trip_to = travel_temp.vietnam.VietnamPackage()
    #        trip_to.detail()

    #   <나> trip_to = vietnam.VietnamPackage()
    #       trip_to.detail()

    #   <다> trip_to = ThailandPackage()
    #        trip_to.detail()