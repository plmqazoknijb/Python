class Entertainer:
    def __init__(self,name):
        self.name=name

    def set_height(self,height):
        self.height=height

    def set_face(self,face):
        self.face=face

    def set_kind(self,kind): #인성
        self.kind=kind

    def set_name(self,name):
        self.name = name

    # def info(self):
    #     print(f'이름: {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성:{self.kind}')

    def __str__(self):
        return f'이름: {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성:{self.kind}'

아이유 = Entertainer('아이유')
# 아이유.set_name('이지은')
아이유.set_height('161cm')
아이유.set_face('형섭쌤 이상형')
아이유.set_kind('That\'s very good')
print(아이유)

윤산하 = Entertainer('윤산하')
윤산하.set_height('185cm')
윤산하.set_face('귀엽고 잘생기고 이쁘고 멋있음')
윤산하.set_kind('막둥이 그 자체')
print(윤산하)

class Singer(Entertainer):
    def __init__(self,name,song):
        super().__init__(name) #self.name = name
        self.song = song

    def __str__(self):
        return super().__str__() +f'\t대표곡: {self.song}'

윤산하 = Singer('윤산하','BadIdea')
윤산하.set_height('185cm')
윤산하.set_face('귀엽고 잘생기고 이쁘고 멋있음')
윤산하.set_kind('막둥이 그 자체')
print(윤산하)

정은지 = Singer('정은지', '하늘바라기')
정은지.set_height('163cm')
정은지.set_face('강아지 상')
정은지.set_kind('That\' very very good')
print(정은지)

class Talent(Entertainer):
    def __init__(self,name,drama):
        super().__init__(name)
        self.drama=drama

    def __str__(self):
        return super().__str__() + f'\t드라마:{self.drama}'

이재욱 = Talent('이재욱','어쩌다 발견한 하루')
이재욱.set_height('187cm')
이재욱.set_face('송은원 이상형')
이재욱.set_kind('순진하고 착함')
print(이재욱)

mj = Singer('김명준', '아니 그래')
mj.set_height('175cm')
mj.set_face('얼굴 개작음')
mj.set_kind('착하고 은근 여리고 또 어른스럽고 웃김')
print(mj)

문빈 = Singer('문빈', 'Knock(널 찾아가)')
문빈.set_height('182cm')
문빈.set_face('섹시한 멍뭉이 상')
문빈.set_kind('강아지 같음')
print(문빈)

아스트로 = []
아스트로.append(mj)
아스트로.append(문빈)
print(아스트로)
