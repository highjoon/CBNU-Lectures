class Student:   #Student라는 클래스를 생성합니다.
    def __init__(self, name=None,highSchool=None, number=0, natScore=0, matScore=0, engScore=0, histScore=0, sci1Score=0, sci2Score=0):
        self.__name=name
        self.__highSchool=highSchool
        self.__number=number
        self.__natScore=natScore
        self.__matScore=matScore
        self.__engScore=engScore
        self.__histScore=histScore
        self.__sci1Score=sci1Score
        self.__sci2Score=sci2Score
        
        #메소드는 이름, 출신고등학교, 수험번호, 국어,수학,영어,국사,탐구1,탐구2로 정의합니다.
        #각 메소드를 초기값으로 설정하기 위해 None과 0으로 정의했습니다.
        
    #학생의 이름을 name메소드로 정의하고 반환합니다.

    def setName(self, name):
        self.__name=name

    def getName(self):
        
        return self.__name

    #학생의 출신고등학교를 highSchool메소드로 정의하고 반환합니다.
    
    def setHighSchool(self, highSchool):
        self.__highSchool=highSchool

    def getHighSchool(self):
        return self.__highSchool

    #학생의 수험번호를 number메소드로 정의하고 반환합니다.
    
    def setNumber(self, number):
        self.__number=number

    def getNumber(self):
        return self.__number

    #학생의 국어점수를 natScore메소드로 정의하고 반환합니다.
    
    def setNatScore(self, natScore):
        self.__natScore=natScore

    def getNatScore(self):
        return self.__natScore

    #학생의 수학점수를 matScore메소드로 정의하고 반환합니다.

    def setMatScore(self, matScore):
        self.__matScore=matScore

    def getMatScore(self):
        return self.__matScore

    #학생의 영어점수를 engScore메소드로 정의하고 반환합니다.

    def setEngScore(self, engScore):
        self.__engScore=engScore

    def getEngScore(self):
        return self.__engScore

    #학생의 국사점수를 histScore메소드로 정의하고 반환합니다.

    def setHistScore(self, histScore):
        self.__histScore=histScore

    def getHistScore(self):
        return self.__histScore

    #학생의 탐구1의점수를 sci1Score메소드로 정의하고 반환합니다.

    def setSci1Score(self, sci1Score):
        self.__sci1Score=sci1Score

    def getSci1Score(self):
        return self.__sci1Score
    
    #학생의 탐구2점수를 sci2Score메소드로 정의하고 반환합니다.

    def setSci2Score(self, sci2Score):
        self.__sci2Score=sci2Score

    def getSci2Score(self):
        return self.__sci2Score

    #입력받은 국어점수를 각 등급으로 구분하는 함수를 생성합니다.

    def calcNatGrade(self):
        if (self.__natScore>90):
            self.__natGrade = "1등급"
            return self.__natGrade
        elif (self.__natScore>80):
            self.__natGrade = "2등급"
            return self.__natGrade
        elif (self.__natScore>70):
            self.__natGrade = "3등급"
            return self.__natGrade
        elif (self.__natScore>60):
            self.__natGrade = "4등급"
            return self.__natGrade
        elif (self.__natScore>50):
            self.__natGrade = "5등급"
            return self.__natGrade
        elif (self.__natScore>40):
            self.__natGrade = "6등급"
            return self.__natGrade
        elif (self.__natScore>30):
            self.__natGrade = "7등급"
            return self.__natGrade
        elif (self.__natScore>20):
            self.__natGrade = "8등급"
            return self.__natGrade
        else:
            self.__natGrade = "9등급"
            return self.__natGrade

    #입력받은 수학점수를 각 등급으로 구분하는 함수를 생성합니다.
            
    def calcMatGrade(self):
        if (self.__matScore>90):
            self.__matGrade = "1등급"
            return self.__matGrade
        elif (self.__matScore>80):
            self.__matGrade = "2등급"
            return self.__matGrade
        elif (self.__matScore>70):
            self.__matGrade = "3등급"
            return self.__matGrade
        elif (self.__matScore>60):
            self.__matGrade = "4등급"
            return self.__matGrade
        elif (self.__matScore>50):
            self.__matGrade = "5등급"
            return self.__matGrade
        elif (self.__matScore>40):
            self.__matGrade = "6등급"
            return self.__matGrade
        elif (self.__matScore>30):
            self.__matGrade = "7등급"
            return self.__matGrade
        elif (self.__matScore>20):
            self.__matGrade = "8등급"
            return self.__matGrade
        else:
            self.__matGrade = "9등급"
            return self.__matGrade
        
    #입력받은 영어점수를 각 등급으로 구분하는 함수를 생성합니다.

    def calcEngGrade(self):
        if (self.__histScore>90):
            self.__engGrade = "1등급"
            return self.__engGrade
        elif (self.__engScore>80):
            self.__engGrade = "2등급"
            return self.__engGrade
        elif (self.__engScore>70):
            self.__engGrade = "3등급"
            return self.__engGrade
        elif (self.__engScore>60):
            self.__engGrade = "4등급"
            return self.__engGrade
        elif (self.__engScore>50):
            self.__engGrade = "5등급"
            return self.__engGrade
        elif (self.__engScore>40):
            self.__engGrade = "6등급"
            return self.__engGrade
        elif (self.__engScore>30):
            self.__engGrade = "7등급"
            return self.__engGrade
        elif (self.__engScore>20):
            self.__engGrade = "8등급"
            return self.__engGrade
        else:
            self.__engGrade = "9등급"
            return self.__engGrade

    #입력받은 국사점수를 각 등급으로 구분하는 함수를 생성합니다.
    #국사 점수의 최대치는 50점입니다.

    def calcHistGrade(self):
        if (self.__histScore>40):
            self.__histGrade = "1등급"
            return self.__histGrade
        elif (self.__histScore>35):
            self.__histGrade = "2등급"
            return self.__histGrade
        elif (self.__histScore>30):
            self.__histGrade = "3등급"
            return self.__histGrade
        elif (self.__histScore>25):
            self.__histGrade = "4등급"
            return self.__histGrade
        elif (self.__histScore>20):
            self.__histGrade = "5등급"
            return self.__histGrade
        elif (self.__histScore>15):
            self.__histGrade = "6등급"
            return self.__histGrade
        elif (self.__histScore>10):
            self.__histGrade = "7등급"
            return self.__histGrade
        elif (self.__histScore>5):
            self.__histGrade = "8등급"
            return self.__histGrade
        else:
            self.__histGrade = "9등급"
            return self.__histGrade
        
    #입력받은 탐구1의 점수를 각 등급으로 구분하는 함수를 생성합니다.
    #탐구1의 점수의 최대치는 50점입니다.

    def calcSci1Grade(self):
        if (self.__sci1Score>40):
            self.__sci1Grade = "1등급"
            return self.__sci1Grade
        elif (self.__sci1Score>35):
            self.__sci1Grade = "2등급"
            return self.__sci1Grade
        elif (self.__sci1Score>30):
            self.__sci1Grade = "3등급"
            return self.__sci1Grade
        elif (self.__sci1Score>25):
            self.__sci1Grade = "4등급"
            return self.__sci1Grade
        elif (self.__sci1Score>20):
            self.__sci1Grade = "5등급"
            return self.__sci1Grade
        elif (self.__sci1Score>15):
            self.__sci1Grade = "6등급"
            return self.__sci1Grade
        elif (self.__sci1Score>10):
            self.__sci1Grade = "7등급"
            return self.__sci1Grade
        elif (self.__sci1Score>5):
            self.__sci1Grade = "8등급"
            return self.__sci1Grade
        else:
            self.__sci1Grade = "9등급"
            return self.__sci1Grade
        
    #입력받은 탐구2의 점수를 각 등급으로 구분하는 함수를 생성합니다.
    #탐구2의 점수의 최대치는 50점입니다.

    def calcSci2Grade(self):
        if (self.__sci2Score>40):
            self.__sci2Grade = "1등급"
            return self.__sci2Grade
        elif (self.__sci2Score>35):
            self.__sci2Grade = "2등급"
            return self.__sci2Grade
        elif (self.__sci2Score>30):
            self.__sci2Grade = "3등급"
            return self.__sci2Grade
        elif (self.__sci2Score>25):
            self.__sci2Grade = "4등급"
            return self.__sci2Grade
        elif (self.__sci2Score>20):
            self.__sci2Grade = "5등급"
            return self.__sci2Grade
        elif (self.__sci2Score>15):
            self.__sci2Grade = "6등급"
            return self.__sci2Grade
        elif (self.__sci2Score>10):
            self.__sci2Grade = "7등급"
            return self.__sci2Grade
        elif (self.__sci2Score>5):
            self.__sci2Grade = "8등급"
            return self.__sci2Grade
        else:
            self.__sci2Grade = "9등급"
            return self.__sci2Grade

        
#king을 참고 학생의 정보로 정의합니다
#입력하는 정보의 순서는 이름, 출신고등학교, 수험번호, 국어점수, 수학점수, 영어점수, 국사점수, 탐구1의점수, 탐구2의점수 순서입니다.
king=Student('참고','광혜원고등학교','2016024053',95,85,75,45,40,35)
#참고 학생은 광혜원고등학교 출신이고, 수험번호는 2016024053입니다.
#국어점수는 95점, 수학점수는 85점, 영어점수는 75점, 국사점수는 45점, 탐구1의 점수는 40점, 탐구2의 점수는 35점입니다.


# 학생의 정보 중 이름, 출신고등학교, 수험번호를 출력합니다.
print('이름:',king.getName(),'출신고등학교',king.getHighSchool(),'수험번호:',king.getNumber())


#신원정보와 각 과목별 성적을 선으로 구분합니다.
print('--------------------------------------------------------------------------')

# 학생의 국어점수와 등급을 출력합니다.
print("국어성적:",king.getNatScore(),"국어등급:",king.calcNatGrade())

# 학생의 수학점수와 등급을 출력합니다.
print("수학성적:",king.getMatScore(),"수학등급:",king.calcMatGrade())

# 학생의 영어점수와 등급을 출력합니다.
print("영어성적:",king.getEngScore(),"영어등급:",king.calcEngGrade())

# 학생의 국사점수와 등급을 출력합니다.
print("국사성적:",king.getHistScore(),"국사등급:",king.calcHistGrade())

# 학생의 탐구1의점수와 등급을 출력합니다.
print("탐구1성적:",king.getSci1Score(),"탐구1등급:",king.calcSci1Grade())

# 학생의 탐구2의점수와 등급을 출력합니다.
print("탐구2성적:",king.getSci2Score(),"탐구2등급:",king.calcSci2Grade())
