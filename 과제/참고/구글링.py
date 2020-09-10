class myScore:
    NUM_OF_STUDENT = 3

    def __init__(self):
        self.name = []
        self.year = []
        self.cls = []
        self.num = []
        self.kor = []
        self.mat = []
        self.eng = []
        self.total = []
        self.avg = []
        self.grade = [0] * self.NUM_OF_STUDENT

    def getScore(self):
        for i in range(0,self.NUM_OF_STUDENT):
            name1 = input(str(i+1) + "번째 학생 이름:")
            kor1 = int(input(str(i+1)+"번째 학생의 국어점수:"))
            mat1 = int(input(str(i+1)+"번째 학생의 수학점수:"))
            eng1 = int(input(str(i+1)+"번째 학생의 영어점수:"))

            self.name.append(name1)
            self.kor.append(kor1)
            self.mat.append(mat1)
            self.eng.append(eng1)

        self.getTotal()
        self.getAvg()
        self.getGrade()

    def getTotal(self):
        for i in range(0,self.NUM_OF_STUDENT):
            total1 = self.kor[i] + self.mat[i] + self.eng[i]
            self.total.append(total1)

    def getAvg(self):
        for i in range(0,self.NUM_OF_STUDENT):
            avg1 = self.total[i] / self.NUM_OF_STUDENT
            self.avg.append(avg1)

    def getGrade(self):
        for i in range(0,self.NUM_OF_STUDENT):
            for j in range(0,self.NUM_OF_STUDENT):
                if self.avg[j] >= self.avg[i]:
                    self.grade[i] += 1


    def print(self):
        for i in range(0,self.NUM_OF_STUDENT):
            print("["+str(i+1)+"]  ["+self.name[i]+"] 학생")
            print("국어 :"+str(self.kor[i]))
            print("영어 :"+str(self.eng[i]))
            print("수학 :"+str(self.mat[i]))
            print()
            print("총점 :"+str(self.total[i]))
            print("평균 :"+str(self.avg[i]))
            print("등수 :"+str(self.grade[i]))
            print()

class myScore2(myScore):
    def printResult(self):
        for i in range(0,self.NUM_OF_STUDENT):
            print("["+str(i+1)+"]"+self.name[i]+"   ",end="")
            for j in range(0,int(self.avg[i]//10)):
                print("*",end="")
            print("   평균 : "+str(self.avg[i]))


result = myScore2()
result.getScore()
result.print()
result.printResult()