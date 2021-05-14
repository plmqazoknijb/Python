from copy import copy

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

# 민혁이꺼 = Drink('초코버블티',3300)
# 민혁이꺼.order()
# print(민혁이꺼)

class Coffee(Drink):
   pass

# 민혁이꺼 = Coffee('아메리카노','3300')
# 민혁이꺼.order()
# print(민혁이꺼)

class Bubbletea(Drink):
    _PEALRS = ('타피오카','코코','젤리','알로에')

    def __init__(self,name,pearl):
        super().__init__(name,pearl)
        self.pearl = 0;

    def set_pearl(self):    #펄종류 보여줌, 펄 선탣
        for index, pearl in enumerate(Bubbletea._PEALRS):
            print(f'{index +1}: {pearl}')
        pearl = input('펄 종류를 선택하세요: ')
        self.ice = 0 if pearl == '' else int(pearl) - 1


    def __str__(self):
        return super().__str__() + f'\t펄:{Bubbletea._PEALRS[self.pearl]}'

    def order(self):
        super().order()
        self.set_pearl()

class Order:
    def __init__(self):
        self.menu =[]
        self.init_menu()
        self.order_menu = []

    def init_menu(self):
        drink1 = Coffee('아메리카노',1800)
        drink2 = Bubbletea('하동녹차오레오',3300)
        drink3 = Bubbletea('딸기요거트',3400)
        self.menu.append(drink1)
        self.menu.append(drink2)
        self.menu.append(drink3)

    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index +1}: {drink.name}\t가격:{drink.price}원')

    def order_drink(self):
        while True:
            self.show_menu()  #메뉴 보여주자#반복 시작
            drink = input('메뉴를 선택하세요 : ')       #메뉴 선택하자
            drink = int(drink) -1
            new_drink = copy(self.menu[drink])
            new_drink.order()           #옵션 선택하자
            self.order_menu.append(new_drink)       #self.order_menu 추가하자
            is_add = input('더 주문하실까요?(n:끝): ')      #더 주문할건지 질문
            if is_add =='n':        #반복 끝
                break
        print(self) #총 가격 계산 후, 주문 내역 보여주기  자기의 __str__() 호출

    def sum_price(self):
        total_price = 0;
        for drink in self.order_menu:       #self.order_menu에서 하나씩 꺼내자
            total_price += drink.price      #음료수.price의 합계를 구하자
        return  total_price

    def __str__(self):  #주문내역
        s='-' *20 + '주문내역' + '-'*20 + '\n'  #주문내역입니다. 제목 보여주자
        for drink in self.order_menu:
            s+= f'{drink}\n'    #self.order_menu 에 있는 음료수 목록 보여주자
        s += f'주문한 음료수 개수: {len(self.order_menu)}개\n'
        s += f'총 가격: {self.sum_price()}원'   #총가격 보여주자
        return s

order = Order()
order.order_drink()