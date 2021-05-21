class Icecream:
    def __init__(self,name,flavor):
        self.name = name
        self.flavor = flavor
        # 이름 : name, 맛:flavor, 설명:description

    def set_description(self,description):
        self.description=description

    def __str__(self):
        return f'이름: {self.name}\t맛: {self.flavor}'

class Cup:
    _CUP_CATEGORIES = ['싱글컵','더블컵','파인트']
    _PRICES = [4000,6200,8200]
    def __init__(self,name,count_flavor):
        self.name = name
        self.count_flavor = count_flavor
        self.price =Cup._PRICES[self.count_flavor-1]
        self.menu = []
        self.add_menu()
        self.order_menu = []

    def add_menu(self):
        아이스홈런볼 = Icecream('아이스홈런볼', '초콜릿,바닐라,피넛')
        아이스홈런볼.set_description('설명 : 초콜릿 아이스크림과 바닐라 아이스크림 속에 초코코팅 홈런볼과 피넛이 들어있다.')
        엄마는외계인 = Icecream('엄마는 외계인', '밀크 초콜릿, 다크 초콜릿, 화이트 무스,초코볼')
        쿠키앤크림 = Icecream('오레오 쿠키 앤 크림', '바닐라,오레오 쿠키')

        self.menu.append(아이스홈런볼)
        self.menu.append(엄마는외계인)
        self.menu.append(쿠키앤크림)

    def show_menu(self):
        for index, icecream in enumerate (self.menu):
            print(index+1,icecream)

    def order(self):
        for n in range(self.count_flavor):
            self.show_menu()
            flavor = input('맛을 고르세요: ')
            flavor = int(flavor)
            icecream = self.menu[flavor-1]
            self.order_menu.append(icecream)
        print('주문한 아이스크림입니다.')
        for icecream in self.order_menu:
            print(icecream)

    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}\t종류: {Cup._CUP_CATEGORIES[self.count_flavor-1]}'

# 동민이꺼 = Cup('더블컵',2)
# print(동민이꺼)
# 동민이꺼.order()

빈이꺼 = Cup('싱글컵',1)
빈이꺼.order()
print(빈이꺼)
