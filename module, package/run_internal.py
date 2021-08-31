import math
print(math.ceil(3.5)) #올림
print(math.ceil(3.4))
print(math.floor(3.5)) #내림
print(math.floor(3.4))
print(round(3.5)) #반올림 math가 아님 주의 ***
print(round(3.4))
print(math.pow(2,10))
print(math.sin(math.pi/2))

import random
print('--------random()----------')
print(random.random())
print(random.randrange(1,10))
print(random.randint(1,10))
list1 = ['김치찌개','비빔면','안먹고 잠']
print(random.choice(list1))

print('before: ', list1)
random.shuffle(list1)
print('after: ',list1)

print(random.sample(list1,2))

import datetime
print('-'*20)
now = datetime.datetime.now()
print(now)
birthday = datetime.datetime(2004,7,2,9,0)
print(birthday)
print(now-birthday)