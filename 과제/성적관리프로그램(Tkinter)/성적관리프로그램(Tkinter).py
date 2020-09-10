"""
성적처리프로그램 만들기

입력: 학생수, 학생이름, 학번, 국어점수, 수학점수, 영어점수

계산: 1. 학생별 총점 및 평균  /  2. 총점기준 석차  /  3. 과목별 석차

출력: 이름 순 / 총점 석차순 / 과목별 석차순 으로 출력하기
"""

"""
● 학생 수는 제한 없습니다.
● 학번은 학년 / 반 / 번호 조합으로 하였습니다. (ex -> 3학년 12반 7번 : 31207)
"""

from tkinter import *

class Student:                              # 모든 진행과정을 포함하는 Student 객체를 생성합니다.
    def __init__(self):
        window = Tk()
        window.title("성적 관리 프로그램")      # Tkinter의 제목과 배경, 크기를 지정합니다.
        window['bg'] = 'lavender'
        window.geometry('650x950+200+200')

        Title = Label(window, text='성적관리프로그램에 오신 것을 환영합니다 !', font="Arial 18 bold italic", relief = 'solid')
        Title['bg'] = 'slate blue'      # 타이틀 Label의 이름과 폰트, 모양, 배경, 전경을 지정하고 격자 배치 합니다.
        Title['fg'] = 'mint cream'
        Title.grid(row=0, padx=72, pady=10, ipadx=10, ipady=10, sticky='W')

        LF = LabelFrame(window, text="학생 정보 입력 :", font="Arial 12 bold italic", relief = 'solid')   # 학생 정보를 입력하는 LabelFrame을 생성하고 격자 배치 합니다.
        LF['bg'] = 'light cyan'
        LF.grid(row=1, columnspan=7, sticky='W', padx=30, pady=5, ipadx=5, ipady=5)

        myInfo = LabelFrame(window, text='작성자 정보 :', font='Arial 12 bold italic', bg = 'powder blue', relief = 'solid')     # 작성자의 정보를 표시하기 위한
        myInfo.grid(row=1, column=0, sticky='W', padx=475, pady=5, ipadx=5, ipady=5)                                            # LabelFarame을 생성합니다.
        Label(myInfo, text='경영정보학과',font='Arial 15 bold italic', bg = 'powder blue').grid(row=1,column=2, sticky='W', padx=5, pady=2)   # 작성자의 정보를
        Label(myInfo, text='20164017', font='Arial 15 bold italic', bg = 'powder blue').grid(row=2, column=2, sticky='W', padx=5, pady=2)   # 표시합니다.
        Label(myInfo, text='윤상준', font='Arial 15 bold italic', bg = 'powder blue').grid(row=3, column=2, sticky='W', padx=5, pady=2)

        Student_info_list = ['이름', '학년', '반', '번호', '국어 점수', '영어 점수', '수학 점수']  # Entry로 입력받을 학생 정보 리스트입니다. 향후 모든 과정에 필요한 필수 정보들입니다.
        r = 1   # 학생 정보의 label을 격자 배치 하기 위한 row 초기 값입니다.

        for info in Student_info_list:  # 반복문을 활용하여 학생 정보 리스트를 Label로 배치하고 이를 격자 배치 합니다.
            Label(LF, text=info, font="Arial 12 bold italic", bg = 'aquamarine', relief = 'solid').grid(row=r, column=0, sticky='E', padx=70, pady=2)
            r += 1

        self.name = StringVar()
        self.grd = StringVar()
        self.cls = IntVar()
        self.num = IntVar()
        self.kr = IntVar()
        self.en = IntVar()
        self.ma = IntVar()

        # 성적 처리에 필요한 항목들 (이름, 학년, 반, 번호, 국어 점수, 영어 점수, 수학 점수)을
        # Label을 이용하여 표시하고,
        # 그 옆에 각 정보를 입력할 수 있도록 Entry로 텍스트 박스를 생성합니다.
        # 인적사항에 입력하는 값들은 정수로 사용되지 않도록 하기 위해 StringVar()로 정의하였습니다.
        # 각 과목의 점수는 정수로 사용되어 등급을 계산하여야 하기 때문에 IntVar()로 정의하였습니다.

        # 각 학생 정보를 입력하기 위한 Entry 항목입니다. 모든 항목의 배경, 모양, 폰트, 크기는 똑같으며 격자배치 구성 역시 똑같습니다.
        self.e1 = Entry(LF, textvariable=self.name, bg='pale green', relief = 'solid', font="Arial 12 bold italic")
        self.e1.grid(row=1, column=1, columnspan=7, sticky="WE", pady=3, padx=5)

        self.e2 = Entry(LF, textvariable=self.grd, bg='pale green', relief = 'solid', font="Arial 12 bold italic")
        self.e2.grid(row=2, column=1, columnspan=7, sticky="WE", pady=3, padx=5)

        self.e3 = Entry(LF, textvariable=self.cls, bg='pale green', relief = 'solid', font="Arial 12 bold italic")
        self.e3.grid(row=3, column=1, columnspan=7, sticky="WE", pady=3, padx=5)
        self.e3.delete(0,END)

        self.e4 = Entry(LF, textvariable=self.num, bg='pale green', relief = 'solid', font="Arial 12 bold italic")
        self.e4.grid(row=4, column=1, columnspan=7, sticky="WE", pady=3, padx=5)
        self.e4.delete(0,END)

        self.e5 = Entry(LF, textvariable=self.kr, bg='pale green', relief = 'solid', font="Arial 12 bold italic")
        self.e5.grid(row=5, column=1, columnspan=7, sticky="WE", pady=3, padx=5)
        self.e5.delete(0, END)

        self.e6 = Entry(LF, textvariable=self.en, bg='pale green', relief = 'solid', font="Arial 12 bold italic")
        self.e6.grid(row=6, column=1, columnspan=7, sticky="WE", pady=3, padx=5)
        self.e6.delete(0, END)

        self.e7 = Entry(LF, textvariable=self.ma, bg='pale green', relief = 'solid', font="Arial 12 bold italic")
        self.e7.grid(row=7, column=1, columnspan=7, sticky="WE", pady=3, padx=5)
        self.e7.delete(0, END)

        # Entry로 입력받은 학생 정보를 등록하기 위한 버튼입니다. 격자 배치 하였습니다.
        # 해당 버튼은 self.show() 함수를 실행합니다. self.show() 함수에서는 Entry로 입력된 학생 정보를 최종적으로 self.S_list에 저장합니다.
        Register = Button(LF, text="학생 등록", width=10, font="Arial 12 bold italic", activebackground="lightgreen",
                          bg = 'light goldenrod', command = lambda:self.show(), relief = 'raised')
        Register.grid(row=9, column=0, sticky=W, pady=4, padx=30)

        # Entry 칸을 비우는 초기화 버튼입니다. 격자 배치 하였습니다.
        # 해당 버튼은 self.reset() 함수를 실행합니다. self.reset() 함수에서는 delete 기능을 사용하여 칸을 비웁니다.
        Reset = Button(LF, text='초기화', width=10, font="Arial 12 bold italic", activebackground="lightgreen",
                       command = lambda:self.reset(), bg = 'moccasin', relief = 'raised')
        Reset.grid(row=9, column=1, sticky=W, pady=4, padx=30)

        # 8가지의 기능을 실행하는 메뉴 보관 LabelFrame을 생성합니다. 격자배치 하였습니다.
        LF1 = LabelFrame(window, text="메뉴 :", font="Arial 12 bold italic", bg = 'lightcyan2', relief = 'solid')
        LF1.grid(row=2, column=0, sticky='W', padx=30, pady=2, ipadx=2, ipady=2)

        # 각각의 기능들이 실행하는 함수의 구동 원리는 향후 밑에서 서술하겠습니다.

        # 1. 전체 학생 목록 출력 기능 버튼입니다. 격자배치 하였으며 self.Print_All_Students() 함수를 실행합니다.
        B1 = Button(LF1, text="1. 전체 학생 목록 출력", width=22, font="Arial 10 bold italic", activebackground="peachpuff2",
                    command = lambda:self.Print_All_Students(), bg = 'light steel blue', relief = 'raised')
        B1.grid(row=2, column=0, sticky=W, pady=4, padx=5)

        # 2. 학생 별 총점 및 평균 출력 기능 버튼입니다. 격자배치 하였으며 self.Print_Total_Avg() 함수를 실행합니다.
        B2 = Button(LF1, text="2. 학생 별 총점 및 평균 출력", width=22, font="Arial 10 bold italic", activebackground="peachpuff2",
                    command = lambda:self.Print_Total_Avg(), bg = 'light steel blue', relief = 'raised')
        B2.grid(row=2, column=1, sticky=W, pady=4, padx=5)

        # 3. 이름 순 정렬 기능 버튼입니다. 격자배치 하였으며 self.sortName() 함수를 실행합니다.
        B3 = Button(LF1, text="3. 이름 순 정렬", width=22, font="Arial 10 bold italic", activebackground="peachpuff2",
                    command = lambda:self.sortName(), bg = 'light steel blue', relief = 'raised')
        B3.grid(row=2, column=2, sticky=W, pady=4, padx=5)

        # 4. 총점 등수 출력 기능 버튼입니다. 격자배치 하였으며 self.sortTotal() 함수를 실행합니다.
        B4 = Button(LF1, text="4. 총점 등수 출력", width=22, font="Arial 10 bold italic", activebackground="peachpuff2",
                    command = lambda:self.sortTotal(), bg = 'light steel blue', relief = 'raised')
        B4.grid(row=3, column=0, sticky=W, pady=4, padx=5)

        # 5. 국어 성적 등수 출력 기능 버튼입니다. 격자배치 하였으며 self.sortKr() 함수를 실행합니다.
        B5 = Button(LF1, text="5. 국어 성적 등수 출력", width=22, font="Arial 10 bold italic", activebackground="peachpuff2",
                    command = lambda:self.sortKr(), bg = 'light steel blue', relief = 'raised')
        B5.grid(row=3, column=1, sticky=W, pady=4, padx=5)

        # 6. 영어 성적 등수 출력 기능 버튼입니다. 격자배치 하였으며 self.sortEn() 함수를 실행합니다.
        B6 = Button(LF1, text="6. 영어 성적 등수 출력", width=22, font="Arial 10 bold italic", activebackground="peachpuff2",
                    command = lambda:self.sortEn(), bg = 'light steel blue', relief = 'raised')
        B6.grid(row=3, column=2, sticky=W, pady=4, padx=5)

        # 7. 수학 성적 등수 출력 기능 버튼입니다. 격자배치 하였으며 self.sortMa() 함수를 실행합니다.
        B7 = Button(LF1, text="7. 수학 성적 등수 출력", width=22, font="Arial 10 bold italic", activebackground="peachpuff2",
                    command = lambda:self.sortMa(), bg = 'light steel blue', relief = 'raised')
        B7.grid(row=4, column=0, sticky=W, pady=4, padx=5)

        # 8. 삭제 기능 버튼입니다. 격자배치 하였으며 Entry에서 입력받은 self.DeleteName 즉, 지우고싶은 사람의 이름을 입력받아 지우는 self.Delete() 함수를 실행합니다.
        Delete = Button(LF1, text="8. 삭제 (이름 입력→)", width=22, font="Arial 10 bold italic", activebackground="peachpuff2",
                    command = lambda:self.Delete(), bg = 'light steel blue', relief = 'raised')
        Delete.grid(row=4, column=1, sticky=W, pady=4, padx=5)

        # 지우고싶은 사람의 이름을 입력하는 self.DeleteName의 Entry입니다. 정수로 사용되지 않도록 하기 위해 StringVar()로 정의하였으며 격자배치 하였습니다.
        self.DeleteName = StringVar()
        self.Delete_Name = Entry(LF1, textvariable=self.DeleteName, bg='pale green', relief = 'solid', font="Arial 12 bold italic")
        self.Delete_Name.grid(row=4, column=2, columnspan=7, sticky="WE", pady=4, padx=5)

        # 프로그램을 종료하는 종료 기능 버튼입니다. 격자배치 하였으며 window.quit 기능을 실행하여 프로그램을 종료합니다.
        QB = Button(window, text='종료', font="Arial 12 bold italic", activebackground="Darkseagreen4", command=window.quit, bg='aquamarine2'
                    , relief = 'raised')
        QB.config(width=59)
        QB.grid(row=5,column=0, sticky = 'W',padx=30)

        # 학생 등록부터 각 기능까지의 모든 기능의 결과물이 출력되는 리스트 박스입니다. 또한 효율적인 구독을 위해 스크롤바를 추가하여 편의성을 높였습니다.
        # 리스트박스와 스크롤바 모두 격자배치하여 위치를 알맞게 조정하였습니다.
        self.list = Listbox(window, width=65, height=20, relief = 'solid')
        scr = Scrollbar(window, orient=VERTICAL, command=self.list.yview, relief = 'solid')
        scr.grid(column=0, rowspan=3, padx=619, sticky='NSW')
        self.list.grid(row=6, column=0, sticky = 'W', rowspan=3, columnspan=1, pady=4, padx=30)
        self.list.config(yscrollcommand=scr.set, font=('Arial', 12, 'bold', 'italic'), bg = 'lightsteelblue1', fg = 'Rosybrown4')


        self.S_list = []    # 학생 정보가 저장되는 리스트 입니다. 이 리스트에 저장된 학생 정보는 모든 기능에 활용됩니다.
        self.num_of_students = 0    # 리스트에 저장되어있는 학생 정보의 수를 나타내는 변수입니다. 초기값은 0으로 설정하였으며, 추가될때에는 +1, 삭제될때는 -1 됩니다.
        mainloop()  # Student 객체의 Tkinter를 실행하는 mainloop() 입니다.

    # 학생 정보를 저장하는 save_Info(self) 함수 입니다. 각 인적사항은 StringVar()로 정의되어 ~.get() 기능으로 불러옵니다.
    # 각 인적사항을 리스트화 하여 self.s 리스트에 저장한 후, 각각의 self.s 리스트를 부모 리스트 (self.S_list)에 저장하는 형식입니다.
    # 인적사항은 차례로 이름, 학번 (학년, 반, 번호 조합), 국어 점수, 영어 점수, 수학 점수, 총점, 평균 순으로 저장됩니다.
    # 저장될 때마다 학생 정보의 수가 +1 되며, "저장 완료! 현재까지 %s명 등록되었습니다!" 의 메시지가 반환됩니다.
    def save_Info(self):
        self.s = [self.name.get(), self.get_St_num(), self.kr.get(), self.en.get(), self.ma.get(), self.getTotal(),
                  self.getAvg()]
        self.S_list.append(self.s)
        self.num_of_students += 1
        return "저장 완료! 현재까지 %s명 등록되었습니다!" % self.num_of_students

    # save_Info(self) 함수의 결과 값 밑 메시지를 리스트박스에 출력하는 show(self) 함수입니다.
    def show(self):
        self.list.insert(END, self.save_Info())

    # 저장된 학생정보를 지우는 Delete(self) 함수 입니다. 먼저 지우고싶은 학생의 이름을 변수 self.DeleteName로 입력 받습니다.
    # 해당 이름을 포함되어있는 self.s 리스트를 찾은 후 self.S_list 에서 해당 self.s 리스트를 삭제하는 방식입니다.
    # 또한 성공적으로 삭제될 때마다 학생 정보의 수가 -1 되며, 리스트박스에는 "학생 정보 삭제 완료! 현재까지 %s명 등록되었습니다!" 가 출력됩니다.
    def Delete(self):
        for i in self.S_list:
            if self.DeleteName.get() in i:
                self.S_list.remove(i)
                self.num_of_students -= 1
                self.list.insert(END, "학생 정보 삭제 완료! 현재까지 %s명 등록되었습니다!" % self.num_of_students)

    # 학번을 계산하는 get_St_num(self) 함수 입니다. 학년, 반, 번호를 참조하며, 형식은 다음과 같습니다.
    # 학년 + 반 ({:02}) + 번호 ({:02}) 형식이며 예시는 다음과 같습니다.
    # 3학년 2반 7번 : 30207
    def get_St_num(self):
        return self.grd.get() + '{:02}'.format(self.cls.get()) + '{:02}'.format(self.num.get())

    # 총점을 계산하는 getTotal(self) 함수 입니다. 국어점수, 영어점수, 수학점수를 참조하며, 세 점수의 총합을 self.total 변수로 반환합니다.
    def getTotal(self):
        self.total = self.kr.get() + self.en.get() + self.ma.get()
        return self.total

    # 평균을 계산하는 getAvg(self) 함수 입니다. self.total 의 총점을 과목 수 (3)로 나눈 후 소숫점 1의자리로 반올림합니다.
    def getAvg(self):
        return round(self.getTotal() / 3,1)

    # Entry에 입력되어있는 값을 초기화하는 reset(self) 함수입니다.
    # delete(0, END) 기능을 사용하여 이름 (e1) 부터 수학 점수 (e7) 까지의 모든 Entry 칸을 비우게 됩니다.
    def reset(self):
        return self.e1.delete(0, END), self.e2.delete(0, END), self.e3.delete(0, END), self.e4.delete(0, END), \
               self.e5.delete(0, END), self.e6.delete(0, END), self.e7.delete(0, END)
    # 1. 전체 학생 목록 출력 기능을 수행하는 Print_All_Students(self) 함수입니다.
    # 반복문을 사용하여 self.S_list 상의 하위 리스트를 인덱싱하여 필요한 값을 출력하며 형식은 다음과 같습니다.
    # "이름 : {} / 학번 : {} / 국어 성적 : {} / 영어 성적 : {} / 수학 성적 : {}"
    def Print_All_Students(self):
        self.list.insert(END, '\n')
        self.list.insert(END, "===============================================================")
        self.list.insert(END, '\n')
        self.list.insert(END, "1. 전체 학생 명단 입니다.")
        self.list.insert(END, '\n')
        for x in range(self.num_of_students):
            self.list.insert(END, ("이름 : {} / 학번 : {} / 국어 성적 : {} / 영어 성적 : {} / 수학 성적 : {}"
                                   .format(self.S_list[x][0], self.S_list[x][1], self.S_list[x][2], self.S_list[x][3]
                                           , self.S_list[x][4], "\n")))
        self.list.insert(END, '\n')
        self.list.insert(END, "===============================================================")

    # 2. 학생 별 총점 및 평균 출력 기능을 수행하는 Print_Total_Avg(self) 함수입니다.
    # 반복문을 사용하여 self.S_list 상의 하위 리스트를 인덱싱하여 필요한 값을 출력하며 형식은 다음과 같습니다.
    # "이름 : {} / 학번 : {} / 총점 : {} / 평균 : {}"
    def Print_Total_Avg(self):
        self.list.insert(END, '\n')
        self.list.insert(END, "===============================================================")
        self.list.insert(END, '\n')
        self.list.insert(END, "2. 학생 별 총점 및 평균 점수 입니다.")
        self.list.insert(END, '\n')
        for x in range(self.num_of_students):
            self.list.insert(END, ("이름 : {} / 학번 : {} / 총점 : {} / 평균 : {}"
                                   .format(self.S_list[x][0], self.S_list[x][1], self.S_list[x][5], self.S_list[x][6],"\n")))

        self.list.insert(END, "===============================================================")

    # 3. 이름 순 정렬 기능을 수행하는 sortName(self) 함수입니다.
    # 먼저 sorted 기능을 활용하여, 학생의 이름을 lambda 값으로 지정한 후, 오름차순으로 정렬하여 sorted_list_Name 리스트에 저장합니다.
    # 이후 반복문을 사용하여 sorted_list_Name 상의 상의 하위 리스트를 인덱싱하여 필요한 값을 출력하며 형식은 다음과 같습니다.
    # "이름 : {} / 학번 : {}"
    def sortName(self):
        sorted_list_Name = sorted(self.S_list, key=lambda x: x[0], reverse = False)
        self.list.insert(END, '\n')
        self.list.insert(END, "===============================================================")
        self.list.insert(END, '\n')
        self.list.insert(END, "3. 이름 순 정렬 입니다.")
        self.list.insert(END, '\n')
        for i in range(self.num_of_students):
            self.list.insert(END, ("이름 : {} / 학번 : {}".format(sorted_list_Name[i][0], sorted_list_Name[i][1])))
        self.list.insert(END, "===============================================================")

    # 4. 총점 등수 출력 기능을 수행하는 sortTotal(self) 함수입니다.
    # 먼저 sorted 기능을 활용하여, 학생의 총점을 lambda 값으로 지정한 후, 내림차순으로 정렬하여 sorted_list_Total 리스트에 저장합니다.
    # 이후 반복문을 사용하여 sorted_list_Total 상의 하위 리스트를 인덱싱하여 필요한 값을 출력하며 형식은 다음과 같습니다.
    # "{}등 : {}점 / 평균 : {}점. (이름 : {} / 학번 : {})"
    def sortTotal(self):
        sorted_list_Total = sorted(self.S_list, key=lambda x: x[5], reverse = True)
        self.list.insert(END, '\n')
        self.list.insert(END, "===============================================================")
        self.list.insert(END, "4. 총점 순 등수 입니다.")
        self.list.insert(END, '\n')
        for i in range(self.num_of_students):
            self.list.insert(END, ("{}등 : {}점 / 평균 : {}점. (이름 : {} / 학번 : {})"
                                   .format(i + 1, sorted_list_Total[i][5], sorted_list_Total[i][6],
                                           sorted_list_Total[i][0], sorted_list_Total[i][1])))

        self.list.insert(END, "===============================================================")

    # 5. 국어 성적 등수 출력 기능을 수행하는 sortKr(self) 함수입니다.
    # 먼저 sorted 기능을 활용하여, 학생의 국어 성적을 lambda 값으로 지정한 후, 내림차순으로 정렬하여 sorted_list_Kr 리스트에 저장합니다.
    # 이후 반복문을 사용하여 sorted_list_Kr 상의 하위 리스트를 인덱싱하여 필요한 값을 출력하며 형식은 다음과 같습니다.
    # "{}등 : {}점. (이름 : {} / 학번 : {})"
    def sortKr(self):
        sorted_list_Kr = sorted(self.S_list, key=lambda x: x[2], reverse = True)
        self.list.insert(END, '\n')
        self.list.insert(END, "===============================================================")
        self.list.insert(END, '\n')
        self.list.insert(END, "5. 국어 성적 순 등수 입니다.")
        self.list.insert(END, '\n')
        for i in range(self.num_of_students):
            self.list.insert(END, ("{}등 : {}점. (이름 : {} / 학번 : {})"
                                   .format(i + 1, sorted_list_Kr[i][2],sorted_list_Kr[i][0], sorted_list_Kr[i][1])))
        self.list.insert(END, "===============================================================")

    # 6. 영어 성적 등수 출력 기능을 수행하는 sortEn(self) 함수입니다.
    # 먼저 sorted 기능을 활용하여, 학생의 영어 성적을 lambda 값으로 지정한 후, 내림차순으로 정렬하여 sorted_list_En 리스트에 저장합니다.
    # 이후 반복문을 사용하여 sorted_list_En 상의 하위 리스트를 인덱싱하여 필요한 값을 출력하며 형식은 다음과 같습니다.
    # "{}등 : {}점. (이름 : {} / 학번 : {})"
    def sortEn(self):
        sorted_list_En = sorted(self.S_list, key=lambda x: x[3], reverse = True)
        self.list.insert(END, '\n')
        self.list.insert(END, "===============================================================")
        self.list.insert(END, '\n')
        self.list.insert(END, "6. 영어 성적 순 등수 입니다.")
        self.list.insert(END, '\n')
        for i in range(self.num_of_students):
            self.list.insert(END, ("{}등 : {}점. (이름 : {} / 학번 : {})"
                                   .format(i + 1, sorted_list_En[i][3],sorted_list_En[i][0], sorted_list_En[i][1])))
        self.list.insert(END, "===============================================================")

    # 7. 수학 성적 등수 출력 기능을 수행하는 sortMa(self) 함수입니다.
    # 먼저 sorted 기능을 활용하여, 학생의 수학 성적을 lambda 값으로 지정한 후, 내림차순으로 정렬하여 sorted_list_Ma 리스트에 저장합니다.
    # 이후 반복문을 사용하여 sorted_list_Ma 상의 하위 리스트를 인덱싱하여 필요한 값을 출력하며 형식은 다음과 같습니다.
    # "{}등 : {}점. (이름 : {} / 학번 : {})"
    def sortMa(self):
        sorted_list_Ma = sorted(self.S_list, key=lambda x: x[4], reverse = True)
        self.list.insert(END, '\n')
        self.list.insert(END, "===============================================================")
        self.list.insert(END, '\n')
        self.list.insert(END, "7. 수학 성적 순 등수 입니다.")
        self.list.insert(END, '\n')
        for i in range(self.num_of_students):
            self.list.insert(END, ("{}등 : {}점. (이름 : {} / 학번 : {})"
                                   .format(i + 1, sorted_list_Ma[i][4],sorted_list_Ma[i][0], sorted_list_Ma[i][1])))
        self.list.insert(END, "===============================================================")

Student()   # Student() 객체로 지정된 Tkinter 을 실행합니다.