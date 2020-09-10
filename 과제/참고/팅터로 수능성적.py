from tkinter import *


#student라는 객체를 생성합니다.
class student:

    
    def __init__(self):

        window=Tk()     #팅터를 실행합니다.
            
        window.title('수능 성적표 만들기')      #팅터의 제목을 수능 성적표 만들기로 지정합니다.

        f=Frame(window)

        f.pack()



        #수능 성적표에 필요한 항목들(수험번호, 성명, 생년월일, 성별, 출신고교, 각 과목별 점수)을
        #Label을 이용하여 레이블로 표시하고,
        #그 아랫줄에 각 정보를 입력할 수 있도록 Entry로 텍스트 박스를 생성합니다.  
        #인적사항에 입력하는 값들은 정수로 사용되지 않도록 하기 위해 StringVar()로 정의하였습니다.
        #각 과목의 점수는 정수로 사용되어 등급을 계산하여야 하기 때문에 IntVar()로 정의하였습니다.
        

        lbname=Label(f,text='학생에 대한 정보를 입력하여 수능 성적표로 정리하는 프로그램입니다.')

        lbname.grid(row=0,column=3)

        self.number=StringVar()

        lbname=Label(f,text='각 항목에 맞는 값들을 입력해주세요.')

        lbname.grid(row=1,column=3)

        self.number=StringVar()
        

        number=Label(f,text='수험번호')

        number.grid(row=2,column=0)

        self.number=StringVar()

        ennumber=Entry(f,textvariable=self.number)

        ennumber.grid(row=3,column=0)

        
        name=Label(f,text='성명')

        name.grid(row=2,column=1)

        self.name=StringVar()

        enname=Entry(f,textvariable=self.name)

        enname.grid(row=3,column=1)
        

        birth=Label(f,text='생년월일')

        birth.grid(row=2,column=2)

        self.birth=StringVar()

        enbirth=Entry(f,textvariable=self.birth)

        enbirth.grid(row=3,column=2)


        sex=Label(f,text='성별')

        sex.grid(row=2,column=3)

        self.sex=StringVar()

        ensex=Entry(f,textvariable=self.sex)

        ensex.grid(row=3,column=3)



        highSchool=Label(f,text='출신고교')

        highSchool.grid(row=2,column=4)

        self.highSchool=StringVar()

        enHighSchool=Entry(f,textvariable=self.highSchool)

        enHighSchool.grid(row=3,column=4)    


        #각 과목을 구분하는 행을 나타내기 위해 '구분'이라는 레이블과
        #각 과목의 점수를 입력하는 행을 나타내기 위해 '원점수'레이블을 추가하였습니다.
        subject=Label(f,text='구분')

        subject.grid(row=4, column=0)

        score=Label(f,text='원점수')

        score.grid(row=5, column=0)


        hist=Label(f,text='국사')

        hist.grid(row=4, column=1)

        self.hist=IntVar()

        enhist=Entry(f,textvariable=self.hist)

        enhist.grid(row=5, column=1)


        kor=Label(f,text='국어')

        kor.grid(row=4, column=2)

        self.kor=IntVar()

        enkor=Entry(f,textvariable=self.kor)

        enkor.grid(row=5, column=2)


        mat=Label(f,text='수학')

        mat.grid(row=4, column=3)

        self.mat=IntVar()

        enmat=Entry(f,textvariable=self.mat)

        enmat.grid(row=5, column=3)

        

        eng=Label(f,text='영어')

        eng.grid(row=4, column=4)

        self.eng=IntVar()

        eneng=Entry(f,textvariable=self.eng)

        eneng.grid(row=5, column=4)


        sci1=Label(f,text='과학탐구1')

        sci1.grid(row=4, column=5)

        self.sci1=IntVar()

        ensci1=Entry(f,textvariable=self.sci1)

        ensci1.grid(row=5, column=5)


        
        sci2=Label(f,text='과학탐구2')

        sci2.grid(row=4, column=6)

        self.sci2=IntVar()

        ensci2=Entry(f,textvariable=self.sci2)

        ensci2.grid(row=5, column=6)


        #입력한 값으로 학생의 인적사항과 과목별 등급을 계산하여 성적표의 형태로 출력하는 버튼을 만듭니다.
        bt1=Button(f,text='성적표 출력',command=self.summary)

        bt1.grid(row=6,column=3)

        btc1=Label(f,text='성적표를 출력하려면 클릭')

        btc1.grid(row=7,column=3)


        #입력한 값들을 초기화시키는 버튼을 만듭니다.
        bt2=Button(f,text='입력값 초기화',command=self.reset)

        bt2.grid(row=6,column=4)

        btc2=Label(f,text='입력값을 초기화 하려면 클릭')

        btc2.grid(row=7,column=4)



    #'성적표 출력'이라는 버튼을 누르면 출력되는 항목으로 학생의 인적사항과 과목별 등급을 계산하여 출력합니다.
    def summary(self):

        #학생의 인적사항인 수험번호, 성명, 생년월일, 성별, 출신고교를 출력합니다.
        print('수험번호:'+self.number.get())
        
        print('성명:'+self.name.get())
        
        print('생년월일:'+self.birth.get())
        
        print('성별:'+self.sex.get())

        print('출신고교:'+self.highSchool.get())


        #국사 등급을 5점 단위로 구분하여 출력합니다.
        if (self.hist.get()>45):
            print("국사 : 1등급")
        elif (self.hist.get()>40):
            print("국사 : 2등급")
        elif (self.hist.get()>35):
            print("국사 : 3등급")
        elif (self.hist.get()>30):
            print("국사 : 4등급")
        elif (self.hist.get()>25):
            print("국사 : 5등급")
        elif (self.hist.get()>20):
            print("국사 : 6등급")
        elif (self.hist.get()>15):
            print("국사 : 7등급")
        elif (self.hist.get()>10):
            print("국사 : 8등급")
        else :
            print("국사 : 9등급")

            
        #국어 등급을 10점 단위로 구분하여 출력합니다.
        if (self.kor.get()>90):
            print("국어 : 1등급")
        elif (self.kor.get()>80):
            print("국어 : 2등급")
        elif (self.kor.get()>70):
            print("국어 : 3등급")
        elif (self.kor.get()>60):
            print("국어 : 4등급")
        elif (self.kor.get()>50):
            print("국어 : 5등급")
        elif (self.kor.get()>40):
            print("국어 : 6등급")
        elif (self.kor.get()>30):
            print("국어 : 7등급")
        elif (self.kor.get()>20):
            print("국어 : 8등급")
        else :
            print("국어 : 9등급")
            

        #수학 등급을 10점 단위로 구분하여 출력합니다.
        if (self.mat.get()>90):
            print("수학 : 1등급")
        elif (self.mat.get()>80):
            print("수학 : 2등급")
        elif (self.mat.get()>70):
            print("수학 : 3등급")
        elif (self.mat.get()>60):
            print("수학 : 4등급")
        elif (self.mat.get()>50):
            print("수학 : 5등급")
        elif (self.mat.get()>40):
            print("수학 : 6등급")
        elif (self.mat.get()>30):
            print("수학 : 7등급")
        elif (self.mat.get()>20):
            print("수학 : 8등급")
        else :
            print("수학 : 9등급")


        #영어 등급을 10점 단위로 구분하여 출력합니다.
        if (self.eng.get()>90):
            print("영어 : 1등급")
        elif (self.eng.get()>80):
            print("영어 : 2등급")
        elif (self.eng.get()>70):
            print("영어 : 3등급")
        elif (self.eng.get()>60):
            print("영어 : 4등급")
        elif (self.eng.get()>50):
            print("영어 : 5등급")
        elif (self.eng.get()>40):
            print("영어 : 6등급")
        elif (self.eng.get()>30):
            print("영어 : 7등급")
        elif (self.eng.get()>20):
            print("영어 : 8등급")
        else :
            print("영어 : 9등급")



        #과학탐구1 등급을 5점 단위로 구분하여 출력합니다.
        if (self.sci1.get()>45):
            print("과학탐구1 : 1등급")
        elif (self.sci1.get()>40):
            print("과학탐구1 : 2등급")
        elif (self.sci1.get()>35):
            print("과학탐구1 : 3등급")
        elif (self.sci1.get()>30):
            print("과학탐구1 : 4등급")
        elif (self.sci1.get()>25):
            print("과학탐구1 : 5등급")
        elif (self.sci1.get()>20):
            print("과학탐구1 : 6등급")
        elif (self.sci1.get()>15):
            print("과학탐구1 : 7등급")
        elif (self.sci1.get()>10):
            print("과학탐구1 : 8등급")
        else :
            print("과학탐구1 : 9등급")



        #과학탐구2 등급을 5점 단위로 구분하여 출력합니다.
        if (self.sci2.get()>45):
            print("과학탐구2 : 1등급")
        elif (self.sci2.get()>40):
            print("과학탐구2 : 2등급")
        elif (self.sci2.get()>35):
            print("과학탐구2 : 3등급")
        elif (self.sci2.get()>30):
            print("과학탐구2 : 4등급")
        elif (self.sci2.get()>25):
            print("과학탐구2 : 5등급")
        elif (self.sci2.get()>20):
            print("과학탐구2 : 6등급")
        elif (self.sci2.get()>15):
            print("과학탐구2 : 7등급")
        elif (self.sci2.get()>10):
            print("과학탐구2 : 8등급")
        else :
            print("과학탐구2 : 9등급")


    #'입력값 초기화' 버튼의 실행작업으로 모든 입력값들을 공백으로 전환합니다.
    def reset(self):

        self.number.set('')

        self.name.set('')
                        
        self.birth.set('')
                        
        self.sex.set('')
                        
        self.highSchool.set('')

        self.hist.set('')

        self.kor.set('')

        self.eng.set('')

        self.mat.set('')

        self.sci1.set('')

        self.sci2.set('')


#student라는 객체로 지정된 팅터를 실행합니다.
student()
mainloop()
