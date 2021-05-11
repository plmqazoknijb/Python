class Drink:
    _CUPS = ('레귤러', '점보')
    _ICES = ('0%', '50%', '100%', '150%')
    _SUGARS = ('0%', '50%', '100%', '150%')

    def __init__(self,name,price): #생성자
        self.name = name
        self.price = price
        self.cup = 0 #Drink._CUPS[0] => '레귤러', Drink._CUPS[1] => '점보'
        self.ice = 2 # Drink._ICES[2] => '100%'
        self.sugar = 2 #Drink._SUGARS[2] => '100%'

    def set_cup(self):
        for index, cup in enumerate(Drink._CUPS):
            print(f'{index+1}:{cup}')
        cup = input('컵사이즈를 선택하세요 : ')#컵 종류 선택하자
        if cup =='':
            self.cup = 0
        else:
            cup = int(cup) -1
            self.cup = cup    #self.cup에 넣자
        if self.cup == 1:     #점보일때 500원 추가
            self.price += 500

    def set_ice(self):
        for index, ice in enumerate(Drink._ICES): # 얼음량 종류 보여주기
            print(f'{index +1}: {ice}')
        ice = input('얼음량을 선택하세요 : ') #얼음량 선택
        self.ice = 2 if ice ==''else int(ice)-1
        # if ice == '':
        #     self.ice = 2
        # else:
        #     self.ice = int(ice)-1 #self.ice에 넣자

    def set_sugar(self):
        for index, sugar in enumerate(Drink._SUGARS):
            print(f'{index +1}: {sugar}')
        sugar = input('당도를 선택하세요 : ')
        self.sugar = 2 if sugar ==''else int(sugar)-1

        #input('0을 누르면 전 단계로 돌아갑니다')
        # if sugar == '0':
        #     self.set_ice()
        #     return          #돌아가게 하는 것

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

    def __str__(self): #문자열 리턴
        return f'이름: {self.name}\t가격: {self.price}원\t컵사이즈: {Drink._CUPS[self.cup]}\t얼음량: {Drink._ICES[self.ice]}\t당도: {Drink._SUGARS[self.sugar]}'

민혁이꺼 = Drink('초코버블티',3300)
민혁이꺼.order()
print(민혁이꺼)

class Coffee(Drink):
   pass

# 민혁이꺼 = Coffee('아메리카노','3300')
# 민혁이꺼.order()
# print(민혁이꺼)

class Bubbletea:
    def __init__(self):
        pass
    def __str__(self):
        pass

class Order:
    def __init__(self):
        pass
    def __str__(self):
        pass
