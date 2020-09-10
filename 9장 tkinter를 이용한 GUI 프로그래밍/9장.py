# pack() -> 위젯의 위치 지정.
# mainloop() -> 윈도우 창을 윈도우가 종료될 때 까지 실행.

# 첫 번째 tkinter 프로그램.
# text를 이름으로 한 버튼 생성.
"""
from tkinter import *

window = Tk()

label = Label(window, text = "Hello World!")
label.pack()

window.mainloop()
"""

# 버튼과 이벤트 처리
# '이것이 파이썬 버튼입니다.'를 이름으로 한 버튼 생성.
"""
from tkinter import *

window = Tk()

b1 = Button(window, text = "이것이 파이썬 버튼입니다.")
b1.pack()

window.mainloop()
"""

# 배치 관리자 소개
# 버튼 생성. 기본적으로 위아래
# 첫 번째 버튼, 두 번째 버튼
"""
from tkinter import *

window = Tk()

b1 = Button(window, text = "첫 번째 버튼")
b2 = Button(window, text = "두 번째 버튼")

b1.pack()
b2.pack()

window.mainloop()
"""

# 배치 관리자 소개
# 버튼 왼쪽 정렬. 눕혀짐. 양옆으로 배치됨
# 첫 번째 버튼, 두 번째 버튼
"""
from tkinter import *

window = Tk()
b1 = Button(window, text="첫번째 버튼")
b2 = Button(window, text="두번째 버튼")
b1.pack(side=LEFT)  
b2.pack(side=LEFT)

window.mainloop()
"""

# 배치 관리자 소개
# 첫 번째 버튼, 두 번째 버튼
# 왼쪽 정렬 & padx 10 부여
# padx -> 위젯에 대한 x 방향 외부 패딩. 가로값. 양 버튼의 간격을 10만큼
# pady -> 위젯에 대한 y 방향 외부 패딩. 세로값.
"""
from tkinter import *

window = Tk()
b1 = Button(window, text="첫번째 버튼")
b2 = Button(window, text="두번째 버튼")
b1.pack(side=LEFT, padx = 10)
b2.pack(side=LEFT, padx = 10)

window.mainloop()
"""


# 버튼의 텍스트 변경
# 첫 번째 버튼, 두 번째 버튼
# 왼쪽 정렬 & padx 10 부여
# 각 버튼의 이름 설정 (One, Two)
"""
from tkinter import *

window = Tk()
b1 = Button(window, text = "첫번째 버튼")
b2 = Button(window, text = "두번째 버튼")
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT, padx = 10)
b1['text'] = "One"
b2['text'] = "Two"

window.mainloop()
"""

# 버튼의 이벤트를 처리하려면
# 콜백 -> 버튼을 누르면 나오는 반응. 이벤트가 발생하면 호출되는 함수.
# 만약 클릭버튼 이벤트가 발생시 호출되는 함수가 있다면 클릭버튼을 눌렀을때 해당 함수가 호출된다.
# '클릭' 버튼 생성 & 왼쪽정렬 & '클릭'버튼이 '버튼이 클릭되었음!'으로 바뀌는 콜백 생성
"""
from tkinter import *

def callback():
    button['text'] = "버튼이 클릭되었음!"

window = Tk()
button = Button(window, text = "클릭", command = callback)
button.pack(side = LEFT)

window.mainloop()
"""


# 예제
# label -> 버튼 위에 제목 설정. 해당 윈도우 창에 표시할 라벨의 속성을 설정
# 안녕하세요! 라벨 생성
# tkinter로 버튼을 쉽게 만들 수 있습니다! 버튼 생성
"""
from tkinter import *

window = Tk()

label = Label(window, text = "안녕하세요!")
label.pack()

button = Button(window, text = "tkinter로 버튼을 쉽게 만들 수 있습니다!")
button.pack()

window.mainloop()
"""

# 클래스로 프레임 감싸기
# App 클래스 생성
# Hello 버튼 생성, Hello 버튼이 클릭되었음! 프린트 콜백 생성, 전경 빨강
# Quit 버튼 생성, Quit 버튼이 클릭되었음! 프린트 콜백 생성
"""
from tkinter import *

class App():
    def __init__(self):
        window = Tk()
        helloB = Button(window, text = "Hello", command = self.hello, fg = 'red')
        helloB.pack()
        quitB = Button(window, text = "Quit", command = self.quit)
        quitB.pack()
        window.mainloop()

    def hello(self):
        print("Hello 버튼이 클릭되었음!")

    def quit(self):
        print("Quit 버튼이 클릭되었음!")
App()
"""

# 단순 위젯과 컨테이너 위젯.
# 위젯은 버튼같은 팅터의 기능.
# 컨테이너는 위젯을 넣을 수 있는 일종의 상자.

# 색상
# 색상: 부분의 위젯은 배경(bg)과 전경(fg) (글씨 색상) 변수를 사용하여 위젯 및 텍스트 색상을 지정

# 버튼을 클릭하세요 버튼 생성
# 전경 노랑, 배경 초록
"""
from tkinter import *

window = Tk()
button = Button(window, text = "버튼을 클릭하세요.")
button.pack()

button['fg'] = 'yellow'
button['bg'] = 'green'

window.mainloop()
"""


# 색상 대화상자
# 사용자에게 색상을 선택하게 한다.
"""
from tkinter import *
from tkinter.colorchooser import *

color = askcolor()
print(color)
"""

# 폰트
# 폰트를 튜플로 지정할 수 있는데 여기에는 (폰트이름, 폰트의 크기, 폰트 스타일)과 같은 형식을 사용한다.
# Times, 10, bold / Helvetica, 10, bold italic / Symbol, 8
"""
("Times", 10, "bold")
("Helvetica", 10, "bold italic")
("Symbol", 8)
"""

# 문자열로도 지정
# Helvatica 라벨 생성. 폰트 = Helvetica, 16
"""
from tkinter import *
window = Tk()
w = Label(window, text='Helvetica', font = 'Helvetica 16')
w.pack()
window.mainloop()
"""

# 예제
# App 클래스 생성
# 커스텀폰트 (Helvetica, 12) 생성
# 버튼 프레임 생성 & Hello, World! 라벨 생성. 커스텀폰트 적용
# 폰트를 크게 버튼 생성 & 폰트 커지는 콜백 적용
# 폰트를 작게 버튼 생성 & 폰트 작아지는 콜백 적용
"""
import tkinter as tk
import tkinter.font as font

class App:
    def __init__(self):
        root=tk.Tk()

        self.customFont = font.Font(family="Helvetica", size=12)

        buttonframe = tk.Frame()
        label = tk.Label(root, text="Hello, World!", font=self.customFont)
        buttonframe.pack()
        label.pack()

        bigger = tk.Button(root, text="폰트를 크게", command=self.BigFont)
        smaller = tk.Button(root, text="폰트를 작게", command=self.SmallFont)
        bigger.pack()
        smaller.pack()
        root.mainloop()

    def BigFont(self):
        size = self.customFont['size']
        self.customFont.configure(size=size+2)

    def SmallFont(self):
        size = self.customFont['size']
        self.customFont.configure(size=size-2)

App()
"""

# 레이블로 화면에 이미지 표시하기
# a1.gif 이미지 불러와 레이블에 표시
# C:\\윤상준\\기타\\기타\\증명사진.jpg

"""
from tkinter import *

window = Tk()
photo = PhotoImage(file="a1.gif")
w = Label(window, image=photo)
w.photo = photo
w.pack()
window.mainloop()
"""

# 레이블에 이미지와 텍스트를 동시에 나타내기
# jusitfy = 라벨의 문자열이 여러 줄 일 경우 정렬 방법 (여기서는 왼쪽정렬) (글 왼쪽정렬)
# 이미지 이름 = wl.gif
# 사진 오른쪽, 글 왼쪽 정렬
# 이미지 넣고 다음 텍스트 삽입
# 텍스트 padx 10 부여
"""
삶이 그대를 속일지라도
슬퍼하거나 노하지 말라 !
우울한 날들을 견디면 : 믿으라,
기쁨의 날이 오리니.
마음은 미래에 사는 것
현재는 슬픈 것:
모든 것은 순간적인 것, 지나가는 것이니
그리고 지나가는 것은 훗날 소중하게 되리니.
"""

"""
from tkinter import *
window = Tk()
photo = PhotoImage(file = 'wl.gif')
w = Label(window, image = photo).pack(side = 'right')
message = \"""
이미지 넣고 다음 텍스트 삽입
삶이 그대를 속일지라도
슬퍼하거나 노하지 말라 !
우울한 날들을 견디면 : 믿으라,
기쁨의 날이 오리니.
마음은 미래에 사는 것
현재는 슬픈 것:
모든 것은 순간적인 것, 지나가는 것이니
그리고 지나가는 것은 훗날 소중하게 되리니.
\"""
w2 = Label(window, text = message, justify = LEFT, padx = 10).pack(side = 'left')
window.mainloop()
"""

# 레이블의 색상과 폰트 변경하기
# Times Font 폰트와 빨강색을 사용합니다., 전경 red, 폰트 Times 32 bold italic
# Helvetica 폰트와 녹색을 사용합니다., 전경 blue, 배경 yellow, 폰트 Helvetica 32 bold italic
"""
from tkinter import *
window = Tk()
Label(window, text = 'Times Font 폰트와 빨강색을 사용합니다.', fg = 'red', font = 'Times 32 bold italic').pack()
Label(window, text = 'Helvetica 폰트와 녹색을 사용합니다.', fg = 'blue', bg = 'yellow', font = 'Helvetica 32 bold italic').pack()
window.mainloop()
"""

# 예제
# 엔트리 위젯
# Entry -> 해당 윈도우 창에 표시할 기입창의 속성을 설정
# 이름, 나이
# 이름, 나이 라벨 격차배치 (row 0, 1)
# 이름, 나이 입력창 (row 0,1 column 1,1)
"""
from tkinter import *
window = Tk()
Label(window, text = '이름').grid(row=0)
Label(window, text = '나이').grid(row=1)
e1=Entry(window)
e2=Entry(window)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
window.mainloop()
"""

# 예제
# sticky	현재 배치된 구역 안에서 특정 위치로 이동. (여기선 서쪽으로 (W))
# pady (y간격 값 수정. 여기에선 4로)
# 이름 홍길동
# 나이 21
# 종료 보이기 버튼 생성 (보이기 격자 (3,1), 서쪽으로 이동, pady=4), (종료 격자(3,0), 서쪽으로 이동, pady=4)
# 라벨, 엔트리 격자배치 (0,1)
"""
from tkinter import *
def show():
    print('이름:%s\n나이:%s' % (e1.get(), e2.get()))
parent = Tk()
Label(parent, text="이름").grid(row=0)
Label(parent, text='나이').grid(row=1)
e1=Entry(parent)
e2=Entry(parent)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
Button(parent,text='보이기',command=show).grid(row=3,column=1,sticky=W,pady=4)
Button(parent,text='종료',command=parent.quit).grid(row=3,column=0,sticky=W,pady=4)
parent.mainloop()
"""

# 텍스트 위젯
# 높이 5, 너비 60의 텍스트창 생성
# insert(END,~)  텍스트의 마지막 문자 위치
# 테스트 위젯은 여러 줄의\n텍스트를 표시할 수 있습니다.
"""
from tkinter import *
window = Tk()
T = Text(window, height = 5, width = 60)
T.pack()
T.insert(END, "테스트 위젯은 여러 줄의\n텍스트를 표시할 수 있습니다.")
window.mainloop()
"""

# Lab: 계산기
# 수식을 텍스트로 입력하면 이것을 평가하고
# 그 결과를 출력할 수 있는 간단한 계산기를 작성하여 본다.
# 수식의 형식은 파이썬과 동일하여야 한다.
# eval() 함수를 사용하여 사용자가 입력한 수식을 계산할 수 있다.
# bind   위젯들의 이벤트와 실행할 함수를 설정
# <Return>	 Enter 키가 입력되었을 때 실행
# 파이썬 수식 입력
# 계산 창
# 결과
"""
from tkinter import *
from math import *
def calculate(event):
    label.configure(text='결과:'+str(eval(entry.get())))
window = Tk()
Label(window, text='파이썬 수식 입력').pack()
entry = Entry(window)
entry.bind('<Return>', calculate)
entry.pack()
label=Label(window, text='결과:')
label.pack()
window.mainloop()
"""

# tkinter를 이용한 그래픽
# 기본적인 구조
# 캔버스 : 선, 다각형, 원등을 그리기 위한 캔버스
# 너비 300, 높이 200의 캔버스 생성
# create_rectangle, create_line 각각 사각형, 선 생성
# rectangle -> 50 * 25, width 200, height 100, 파랑색
# line -> (0,0) 부터 (300,200)까지 하나, (0,0) 부터 (300,100)까지 하나 (빨간색)
"""
from tkinter import *
window = Tk()
w = Canvas(window,width=300,height=200)
w.pack()
w.create_rectangle(50,25,200,100,fill='blue')
w.create_line(0,0,300,200)
w.create_line(0,0,300,100,fill='red')
window.mainloop()
"""

# Lab: 랜덤한 사각형 그리기
# 윈도우를 하나 만들고 여기에 랜덤한 크기의 사각형을 여러 개 그려보자.
# 위치도 랜덤이어야 하고 크기, 색상도 랜덤으로 하여 본다.
# rectangle -> 사각형
# 캔버스 너비 500 높이 400
# 색 : "red", "orange", "yellow", "green", "blue", "violet"
# 10번 실행
# x = 0~500, y = 0~400, w = 100, z = 100
"""
import random
from tkinter import *
window = Tk()
canvas = Canvas(window, width=500, height=400)
canvas.pack()
color=["red", "orange", "yellow", "green", "blue", "violet"]
def draw_rect():
    x = random.randint(0,500)
    y = random.randint(0,400)
    w = random.randrange(100)
    z = random.randrange(100)
    canvas.create_rectangle(x,y,w,z,fill=random.choice(color))
for i in range(10):
    draw_rect()
mainloop()
"""

# 타원 그리기
# 캔버스 너비 300, 높이 200
# oval -> 타원, (10,10)위치에서 (200,150)의 크기를 가지는 타원
"""
from tkinter import *
window = Tk()
canvas = Canvas(window, width = 300, height = 200)
canvas.pack()
canvas.create_oval(10,10,200,150)
mainloop()
"""

# 호 그리기
# 캔버스 너비 300, 높이 200
# arc -> 호, (x1, y1)에서 (x2, y2)의 크기를 가지며 start 각도부터 extent의 각을 지니는 호 생성
# (10,10)위치에서 (200,150)의 크기를 가지며 90도, 아크형태
"""
from tkinter import *
window = Tk()
canvas = Canvas(width=300,height=200)
canvas.pack()
canvas.create_arc(10,10,200,150,extent=90,style=ARC)
mainloop()
"""

# 다각형 그리기
# 캔버스 너비 300, 높이 200
# (10, 10), (150, 110), (250, 20)의 꼭지접을 갖는 다각형 생성
# polygon -> 다각형, (x1, y1), (x2, y2), …, (xn, yn) 의 꼭지점을 갖는 다각형.
# 파랑색
"""
from tkinter import *
window = Tk()
canvas = Canvas(window, width = 300, height = 200)
canvas.pack()
canvas.create_polygon(10,10,150,100,250,20,fill='blue')
mainloop()
"""

# 텍스트 그리기
# 너비 300, 높이 200 캔버스 생성
# (100, 100) 위치에 '싱 스트리트(Sing Street)' 텍스트 생성
"""
from tkinter import *
window = Tk()
canvas = Canvas(window, width = 300, height = 200)
canvas.pack()
canvas.create_text(100,100,text='싱 스트리트(Sing Street)')
mainloop()
"""

# 이미지 그리기
# 너비 300, 높이 200 캔버스 생성
# (20,20)위치에 D:\\starship.png 이미지 삽입
# anchor : 위치지정 (여기선 북서쪽(NW))
"""
from tkinter import *
window = Tk()
canvas = Canvas(window,width=300,height=200)
canvas.pack()
img=PhotoImage(file='D:\\starship.png')
canvas.create_image(20,20,image=img,anchor=NW)
mainloop()
"""

# 애니메이션을 만들어 보자.
# 너비 400, 높이 300 캔버스 생성
# (10,100)위치에 (50,150)의 크기를 갖는 타원 생성 (초록색)
# 해당 타원을 100번 움직이자.
# move : 해당 객체를 (x,y)만큼 이동. (여기서는 (3,0)만큼 이동)
# update : 화면 업데이트
# time.sleep(0.05) : 0.05초만큼 시간 제어 (한번 움직일때마다 0.05초 소요)
"""
import time
from tkinter import *
window = Tk()
canvas = Canvas(window,width=400,height=300)
canvas.pack()
id=canvas.create_oval(10,100,50,150,fill='green')
for i in range(100):
    canvas.move(id,3,0)
    window.update()
    time.sleep(0.05)
"""

# 화살표 키로 공을 움직여 보자.
# 너비 400, 높이 300 캔버스 생성
# (10,100)위치에 (50,150)의 크기를 갖는 타원 생성 (초록색)
# 오른쪽으로 5씩 이동하는 함수 생성
# bind_all : 이벤트 핸들러 설정
"""
from tkinter import *
window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()
id = canvas.create_oval(10,100,50,150,fill='green')
def move_right(event):
    canvas.move(id,5,0)
canvas.bind_all('<KeyPress-Right>',move_right)
mainloop()
"""

# Lab: 마우스로 그림 그리기
# 다음과 같이 마우스를 움직여서 화면에 그림을 그리는 애플리케이션을 작성해보자.
# 너비 500, 높이 300의 캔버스 생성
# DrawDot 함수 생성
# event - 1 : 마우스 왼쪽 버튼 누르는 위치
# event + 1 : 마우스 오른쪽 버튼 누르는 위치
# 마우스 클릭한 곳에 타원 생성 (빨간색)
# fill = 채우기 (BOTH : 요구되었지만 사용되지 않은 공간을 확인할수 있다.)
# expand = 요구되지 않은공간 사용하기 (YES : 요구되지 않은공간을 사용)
# B1-Motion : 마우스 왼쪽 버튼을 누르면서 움직일 때
# 제목 : "마우스를 드래그하면 점들이 그려집니다." 의 라벨 생성
# 맨 아래에 배치 (BOTTOM)
"""
from tkinter import *
w = 500
h = 300
def drawDot(event):
    x1,y1 = (event.x-1),(event.y-1)
    x2,y2 = (event.x+1),(event.y+1)
    canvas.create_oval(x1,y1,x2,y2,fill='red')
window = Tk()
canvas = Canvas(window, width=w, height=h)
canvas.pack(fill=BOTH, expand=YES)
canvas.bind('<B1-Motion>',drawDot)
label=Label(window,text='마우스를 드래그하면 점들이 그려집니다.')
label.pack(side=BOTTOM)
mainloop()
"""

# 라디오 버튼
# 라디오 버튼(radio button)은 체크 박스와 비슷하지만
# 하나의 그룹 안에서는 한 개의 버튼만 선택할 수 있다는 점이 다르다.
# IntVar() : 체크박스 위젯
# anchor	라디오버튼안의 문자열 또는 이미지의 위치
# justify	라디오버튼의 문자열이 여러 줄 일 경우 정렬 방법
# 제목 : 가장 선호하는 프로그래밍 언어를 선택하시오 의 라벨 생성 (왼쪽 정렬, 20 x값 이동)
# 선택지 : Python, C, Java, Swift
# 모두 W로 위치지정
# variable = tkinter.IntVar()의 그룹이 같을 경우 하나의 묶음으로 간주하며 ‘value’의 값이 저장됨.
# value = 각각 다르게 (value를 이용하여 라디오버튼의 값을 설정, 숫자 같으면 같이 선택됨)
# 라디오 버튼 예제
"""
from tkinter import *
window=Tk()
choice=IntVar()
Label(window,text='가장 선호하는 프로그래밍 언어를 선택하시오',justify=LEFT,padx=20).pack()
Radiobutton(window,text='Python',variable=choice,value=1).pack(anchor=W)
Radiobutton(window,text='C',variable=choice,value=2).pack(anchor=W)
Radiobutton(window,text='Java',variable=choice,value=3).pack(anchor=W)
Radiobutton(window,text='Swift',variable=choice,value=4).pack(anchor=W)
mainloop()
"""

# 체크 박스
# 체크 박스(check box)란 사용자가 클릭하여서
# 체크된 상태와 체크되지 않은 상태 중의 하나로 만들 수 있는 위젯이다.
# 라벨 제목 : 선호하는 언어를 모두 선택하시오.
# 격자배치
# 파이썬, C, 자바, 스위프트

# 체크 버튼 예제
"""
from tkinter import *
window=Tk()
Label(window,text="선호하는 언어를 모두 선택하시오").grid(row=0,sticky=W)
value1=IntVar()
value2=IntVar()
value3=IntVar()
value4=IntVar()
Checkbutton(window,text='Python',variable=value1).grid(row=1,sticky=W)
Checkbutton(window,text='C',variable=value2).grid(row=2,sticky=W)
Checkbutton(window,text='Java',variable=value3).grid(row=3,sticky=W)
Checkbutton(window,text='Swift',variable=value4).grid(row=4,sticky=W)
mainloop()
"""

# 리스트 박스
# 높이 4의 리스트박스 생성
# python, c, java, swift 삽입
"""
from tkinter import *
window=Tk()
lb=Listbox(window,height=4)
lb.pack()
lb.insert(END,'python')
lb.insert(END,'C')
lb.insert(END,'Java')
lb.insert(END,'Swift')
mainloop()
"""

# 배치 관리자
# 배치 관리자는 컨테이너 안에 존재하는
# 위젯의 크기와 위치를 자동적으로 관리하는 객체이다.

# 격자 배치 관리자
# 격자 배치 관리자(grid geometry manager)는 위젯 (버튼, 레이블 등)을 테이블 형태로 배치한다.
# 버튼(One)을 (0,0)에 , 버튼(Two)을 (1,1)에 배치
"""
from tkinter import *
window=Tk()
b1=Button(window,text='One')
b2=Button(window,text='Two')
b1.grid(row=0,column=0)
b2.grid(row=1,column=1)
mainloop()
"""

# 압축 배치 관리자
# 압축 배치 관리자(pack geometry manager)는 위젯들을 부모 위젯 안에 압축.
# 라벨 박스#1,2,3 생성 각각 (배경 빨강, 전경 하양), (배경 초록, 전경 검정), (배경 파랑, 전경 하양)
"""
from tkinter import *
window = Tk()
Label(window,text='박스#1',bg='red',fg='white').pack()
Label(window,text='박스#2',bg='green',fg='black').pack()
Label(window,text='박스#3',bg='blue',fg='white').pack()
mainloop()
"""

# 절대 위치 배치 관리자
# 라벨 박스#1,2,3 생성 각각 (배경 빨강, 전경 하양, (0,0)배치), (배경 초록, 전경 검정, (20,20)배치), (배경 파랑, 전경 하양 (40,40)배치)
"""
from tkinter import *
window=Tk()
w=Label(window,text='박스#1',bg='red',fg='white')
w.place(x=0,y=0)
w=Label(window,text='박스#2',bg='green',fg='black')
w.place(x=20,y=20)
w=Label(window,text='박스#3',bg='blue',fg='white')
w.place(x=40,y=40)
mainloop()
"""

# Lab: 틱택토
# Tic-Tac-Toe는 3×3칸을 가지는 게임판을 만들고,
# 경기자 2명이 동그라미 심볼(O)와 가위표 심볼(X)을 고른다.
# 경기자는 번갈아 가며 게임판에 동그라미나 가위표를 놓는다.
# 가로, 세로, 대각선으로 동일한 심볼을 먼저 만들면 승리하게 된다.
"""
from tkinter import *
def checked(i):
    global player
    button=list[i]
    if button['text'] != '            ':
        return
    button['text']='     '+player+'      '
    button['bg']='yellow'
    if player=='X':
        player='O'
        button['bg']='yellow'
    else:
        player='X'
        button['bg']='lightgreen'
window=Tk()
player='X'
list=[]
for i in range(9):
    b=Button(window,text='            ',command=lambda k=i: checked(k))
    b.grid(row=i//3,column=i%3)
    list.append(b)
mainloop()
"""

# Lab: 마우스로 그림 그리기
# 격자 배치 관리자를 사용하여 레이블과 버튼을 배치한다.
# 색상의 개수만큼 반복하면서 레이블과 버튼을 생성하고 격자형태로 배치하면 된다.
# relief	프레임의 테두리 모양 (RIDGE = 경계선만 볼록하게)
# 색 : 'green', 'red', 'orange','white','yellow','blue'
# 라벨 너비 15, 버튼 너비 10
"""
from tkinter import *
window=Tk()
colors=['green', 'red', 'orange','white','yellow','blue']
r=0
for c in colors:
    Label(window,text=c,width=15,relief=RIDGE).grid(row=r,column=0)
    Button(window,bg=c,width=10).grid(row=r,column=1)
    r += 1
mainloop()
"""

# Lab: 스톱워치 만들기
# 레이블을 사용하여 간단한 스톱워치를 작성하여 보자.
# 시작 버튼을 누르면 시작되고 중지 버튼을 누르면 스톱워치가 중지된다.
# 시작버튼, 종료버튼 배경 노랑색
# after(time,callback) : time 마이크로세컨드 뒤에 callback
# 타이머 폰트 : "Helvetica", 80

# Lab: 계산기 만들기
"""
import tkinter as tk
def startTimer():
    if (running):
        global timer
        timer += 1
        timerText.configure(text=str(timer))
    window.after(10,startTimer)
def start():
    global running
    running = True
def stop():
    global running
    running = False
running = False

window=tk.Tk()
timer = 0
timerText = tk.Label(window,text='0',font=('Helvetica',80))
timerText.pack()
startButton=tk.Button(window,text='시작',bg='yellow',command=start)
startButton.pack(fill=tk.BOTH)
stopButton=tk.Button(window,text='스톱',bg='yellow',command=stop)
stopButton.pack(fill=tk.BOTH)

startTimer()
window.mainloop()
"""

# 파이썬을 이용하여 버튼을 가지는 계산기를 작성하여 보자. 적절한 배치 관리자를 선택하여 사용하라.
# 계산기 창 제목 : 간단한 계산기
# try, except
# 계산기 버튼
# buttons = [
# '7',  '8',  '9',  '+',  'C',
# '4',  '5',  '6',  '-',  '  ',
# '1',  '2',  '3',  '*',  '  ',
# '0',  '.',  '=',  '/',  '   ' ]
# 버튼 너비 5, 모서리 뭉툭하게 (RIDGE)
# 엔트리 너비 33, 배경 노랑색
# columnspan = 차지하는 열의 크기
"""
from tkinter import *
def click(key):
    if key == '=':
        try:
            result=eval(entry.get())
            entry.delete(0,END)
            entry.insert(END,str(result))
        except:
            entry.insert(END,'오류!')
    elif key == 'C':
        entry.delete(0,END)
    else:
        entry.insert(END,key)
window=Tk()
window.title("간단한 계산기")
i=0
buttons = [
 '7',  '8',  '9',  '+',  'C',
 '4',  '5',  '6',  '-',  '  ',
 '1',  '2',  '3',  '*',  '  ',
 '0',  '.',  '=',  '/',  '   ' ]
for b in buttons:
    cmd = lambda x=b: click(x)
    b = Button(window, text=b,width=5,relief='ridge',command=cmd)
    b.grid(row=i//5+1,column=i%5)
    i += 1
entry=Entry(window,width=33,bg='yellow')
entry.grid(row=0,column=0,columnspan=5)
window.mainloop()
"""

# 마우스 이벤트 처리
# 32 44 에서 마우스 이벤트 발생
# 6 52 에서 마우스 이벤트 발생
# 너비, 높이 100인 프레임 생성
"""
from tkinter import *
def callback(event):
    print(event.x,event.y,'에서 마우스 이벤트 발생')
window=Tk()
frame=Frame(window,width=100,height=100)
frame.bind('<Button-1>',callback)
frame.pack()
window.mainloop()
"""

# 키보드 이벤트 처리
# 66 31 에서 마우스 이벤트 발생
# 'k' 가 눌렸습니다.
# 너비 높이 100인 프레임 생성
# focus_set()   포커스 설정
"""
from tkinter import *
def key(event):
    print(repr(event.char),"가 눌렸습니다.")
def callback(event):
    frame.focus_set()
    print(event.x,event.y,"에서 마우스 이벤트 발생")
window=Tk()
frame = Frame(window,width=100,height=100)
frame.bind('<Key>',key)
frame.bind('<Button-1>',callback)
frame.pack()
mainloop()
"""

# 마우스 버튼 이벤트 처리
# 단일 클릭, 왼쪽 버튼
# 단일 클릭, 왼쪽 버튼
# 더블 클릭, 왼쪽 버튼
"""
from tkinter import *

def sleft(event):
    print("단일클릭, 왼쪽버튼")
def dleft(event):
    print("더블클릭, 왼쪽버튼")
widget=Button(None,text='마우스 클릭')
widget.pack()

widget.bind('<Button-1>',sleft)
widget.bind('<Double-1>',dleft)
mainloop()
"""

# 마우스 모션 이벤트 처리
# 마우스 위치: (274 45)
# 마우스 위치: (271 55)
# 마우스 위치: (270 69)
# message = """당신 스스로가 하지 않으면 아무도 당신의 운명을 개선시켜주지 않을 것이다. """
# 메시지 배경 노랑, 전경 파랑, 폰트 "times 20 italic"
"""
from tkinter import *
def motion(event):
    print("마우스 위치: (%s, %s)" % (event.x,event.y))
message = \"""당신 스스로가 하지 않으면 아무도 당신의 운명을 개선시켜주지 않을 것이다. \"""
window=Tk()
msg=Message(window,text=message)
msg.configure(bg='yellow',fg='blue',font='times 20 italic')
msg.bind('<Motion>',motion)
msg.pack()
mainloop()
"""

# Lab: 숫자 추측 게임
# 사용자가 컴퓨터가 생성한 숫자(1부터 100사이의 난수)를 알아맞히는 게임을
# 그래픽 사용자 인터페이스를 사용하여 제작해보자.
# 윈도우 배경 흰색
# 창 제목 : 숫자 맞추기, 창 크기 = 500x80
# 라벨 제목 : 숫자 게임에 오신 것을 환영합니다!, 배경 흰색
# 시도 버튼, 전경 초록, 배경 흰색 / 초기화 버튼, 전경 빨강, 배경 흰색
# 결과라벨 배경 흰색
"""
from tkinter import *
import random

answer = random.randint(1,100)

def guessing():
    guess=int(guessField.get())
    if guess > answer:
        msg='높음'
    elif guess < answer:
        msg='낮음'
    else:
        msg='정답'
    resultLabel['text']=msg
    guessField.delete(0,5)
def reset():
    global answer
    answer = random.randint(1,100)
    resultLabel['text']='다시 하세요'
window = Tk()
window.configure()
window.title('숫자 맞추기')
window.geometry('500x80')

titleLabel=Label(window,text='숫자 게임에 오신 것을 환영합니다!', bg='white')
titleLabel.pack()

guessField=Entry(window)
guessField.pack(side='left')
tryButton=Button(window,text='시도',fg='green',bg='white',command=guessing)
tryButton.pack(side='left')

resetButton=Button(window,text='초기화',fg='red',bg='white',command=reset)
resetButton.pack(side='left')
resultLabel=Label(window, text='1부터 100사이 입력하시오.',bg='white')
resultLabel.pack(side='left')

mainloop()
"""