class Tiger:
    def Jump(self):
        print("호랑이처럼 멀리 점프하기")

class Lion:
    def Bite(self):
        print("사자처럼 한입에 꿀꺽하기")

class Liger (Tiger, Lion):      # 다중 상속
    def play(self):
        print("라이거만의 사육사와 재미있게 놀기")