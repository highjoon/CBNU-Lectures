"""
성적처리프로그램 만들기

입력: 학생수, 학생이름, 학번, 국어점수, 수학점수, 영어점수

계산: 1. 학생별 총점 및 평균  /  2. 총점기준 석차  /  3. 과목별 석차

출력: 이름 순 / 총점 석차순 / 과목별 석차순 으로 출력하기
"""

"""

● 학생 수는 4명으로 설정하였습니다.
● 학번은 학년 / 반 / 번호 조합으로 하였습니다. (ex -> 3학년 12반 7번 : 31207)

"""

# 모든 메소드는 정보 은닉을 활용하여 생성되었습니다.
class Student:  # Student의 클래스를 생성합니다. 향후 진행될 처리의 기반 클래스입니다.
    Num_of_Students = 4     # 총 4명의 학생을 등록한다는 의미입니다.
    def __init__(self,name, year, cls, num, kr, en, ma):
        self.__name= name
        self.__year = year
        self.__cls = cls
        self.__num = num
        self.set_st_num()
        self.__kr= kr
        self.__en= en
        self.__ma= ma
        self.get_total()
        self.get_avg()

    # 메소드는 이름, (학년, 반, 번호,) 학번, 국어, 수학, 영어, 총점, 평균 순으로 정의합니다.

    # 각 메소드는 접근자, 설정자 메소드를 활용하여 정의 및 반환합니다.
    def __repr__(self):
        return '[{} / 학번 : {} / 국어 : {} / 영어 : {} / 수학 : {} / 총점 : {} / 평균 : {}]'\
        .format(self.__name, self.set_st_num(), self.__kr, self.__en, self.__ma, self.get_total(),
                self.get_avg())

    def setname(self, name):    # 학생의 이름을 name메소드로 정의 및 반환합니다.
        self.__name = name

    def getname(self):
        return self.__name

    def setyear(self, year):    # 학생의 년도를 year메소드로 정의 및 반환합니다.
        self.__year = year

    def getyear(self):
        return self.__year

    def setcls(self, cls):      # 학생의 반을 cls메소드로 정의 및 반환합니다.
        self.__cls = cls

    def getcls(self):
        return self.__cls

    def setnum(self, num):      # 학생의 번호를 num메소드로 정의 및 반환합니다.
        self.__num = num

    def getnum(self):
        return self.__num

    def setkr(self, kr):        # 학생의 국어점수를 kr메소드로 정의 및 반환합니다.
        self.__kr = kr

    def getkr(self):
        return self.__kr

    def seten(self, en):        # 학생의 영어점수를 en메소드로 정의 및 반환합니다.
        self.__en = en

    def geten(self):
        return self.__en

    def setma(self, ma):        # 학생의 수학점수를 ma메소드로 정의 및 반환합니다.
        self.__ma = ma

    def getma(self):
        return self.__ma

    def get_info(self):         # 오브젝트의 필드 정보를 하나의 str으로 묶는 함수입니다.
        return '{} / 학번 : {} / 국어 : {}점 / 영어 : {}점 / 수학 : {}점 / 총점 : {}점 / 평균 : {}점'\
            .format(self.__name, self.set_st_num(), self.__kr, self.__en, self.__ma, self.get_total(),
                    self.get_avg())

    def print_student(self):    # 오브젝트의 필드 정보를 출력하는 함수입니다.
                                # 정보들을 str으로 변환하는 작업은 get_info()에게 맡겼습니다.
        print(self.get_info())

    def set_st_num(self):       # 학번은 학년 / 반 / 번호 조합으로 하였습니다. (ex -> 3학년 12반 7번 : 31207)
        self.__st_num = self.__year + '{:02}'.format(self.__cls) + '{:02}'.format(self.__num)
        return self.__st_num

    def get_total(self):        # 학생의 국어, 영어, 수학 점수 총합을 total메소드로 정의 및 반환합니다.
        self.__total = self.__kr + self.__en + self.__ma
        return self.__total

    def get_avg(self):          # 학생의 국어, 영어, 수학 점수 평균을 avg메소드로 정의 및 반환합니다.
        self.__avg = round(self.__total / 3,1)
        return self.__avg

    def print_total_avg(self):  # 학생의 총점과 평균을 보여주기 위한 함수입니다.
        print('{} / 학번 : {} / 총점 : {}점 / 평균 : {}점'
              .format(self.__name, self.__st_num, self.__total, self.__avg))

    # 동일한 학생의 정보를 활용하여 정렬 및 순위구하기 작업을 하기 위해 중첩 클래스를 활용하였습니다.

    class Student_name:     # 이름 순 정렬을 위한 중첩클래스 입니다.
        def __init__(self,name,year,cls,num):
            self.__name = name
            self.__year = year
            self.__cls = cls
            self.__num = num
            self.set_st_num()

        def setname(self, name):    # 이름 순 정렬을 위해 이름을 name메소드로 정의 및 반환합니다.
            self.__name = name

        def getname(self):
            return self.__name

        def setyear(self, year):    # 이름 순 정렬을 위해 학년을 year메소드로 정의 및 반환합니다.
            self.__year = year

        def getyear(self):
            return self.__year

        def setcls(self, cls):    # 이름 순 정렬을 위해 반을 cls메소드로 정의 및 반환합니다.
            self.__cls = cls

        def getcls(self):
            return self.__cls

        def setnum(self, num):    # 이름 순 정렬을 위해 번호를 num메소드로 정의 및 반환합니다.
            self.__num = num

        def getnum(self):
            return self.__num

        def set_st_num(self):    # 이름 순 정렬을 위해 학번을 생성하는 함수입니다.
            self.__st_num = self.__year + '{:02}'.format(self.__cls) + '{:02}'.format(self.__num)
            return self.__st_num

    class Student_total:     # 총점 순 정렬을 위한 중첩클래스 입니다.
        def __init__(self,name,year,cls,num, kr, en, ma):
            self.__name = name
            self.__year = year
            self.__cls = cls
            self.__num = num
            self.set_st_num()
            self.__kr = kr
            self.__en = en
            self.__ma = ma
            self.get_total()
            self.get_avg()

        def setname(self, name):    # 총점 순 정렬을 위해 이름을 name메소드로 정의 및 반환합니다.
            self.__name = name

        def getname(self):
            return self.__name

        def setyear(self, year):    # 총점 순 정렬을 위해 학년을 year메소드로 정의 및 반환합니다.
            self.__year = year

        def getyear(self):
            return self.__year

        def setcls(self, cls):    # 총점 순 정렬을 위해 반을 cls메소드로 정의 및 반환합니다.
            self.__cls = cls

        def getcls(self):
            return self.__cls

        def setnum(self, num):    # 총점 순 정렬을 위해 번호를 num메소드로 정의 및 반환합니다.
            self.__num = num

        def getnum(self):
            return self.__num

        def set_st_num(self):    # 총점 순 정렬을 위해 학번을 생성하는 함수입니다.
            self.__st_num = self.__year + '{:02}'.format(self.__cls) + '{:02}'.format(self.__num)
            return self.__st_num

        def setkr(self, kr):  # 총점순 등수를 위해 국어점수를 kr메소드로 정의 및 반환합니다.
            self.__kr = kr

        def getkr(self):
            return self.__kr

        def seten(self, en):  # 총점순 등수를 위해 영어점수를 en메소드로 정의 및 반환합니다.
            self.__en = en

        def geten(self):
            return self.__en

        def setma(self, ma):  # 총점순 등수를 위해 수학점수를 ma메소드로 정의 및 반환합니다.
            self.__ma = ma

        def getma(self):
            return self.__ma

        def get_total(self):  # 총점순 등수를 위해 국어, 영어, 수학 점수 총합을 total메소드로 정의 및 반환합니다.
            self.__total = self.__kr + self.__en + self.__ma
            return self.__total

        def get_avg(self):  # 총점순 등수를 위해 국어, 영어, 수학 점수 평균을 avg메소드로 정의 및 반환합니다.
            self.__avg = round(self.__total / 3, 1)
            return self.__avg

    class Student_kr:     # 국어점수 순 정렬을 위한 중첩클래스 입니다.
        def __init__(self,name,year,cls,num,kr):
            self.__name = name
            self.__year = year
            self.__cls = cls
            self.__num = num
            self.set_st_num()
            self.__kr = kr

        def setname(self, name):    # 국어점수 등수를 위해 이름을 name메소드로 정의 및 반환합니다.
            self.__name = name

        def getname(self):
            return self.__name

        def setyear(self, year):    # 국어점수 등수를 위해 학년을 year메소드로 정의 및 반환합니다.
            self.__year = year

        def getyear(self):
            return self.__year

        def setcls(self, cls):    # 국어점수 등수를 위해 반을 cls메소드로 정의 및 반환합니다.
            self.__cls = cls

        def getcls(self):
            return self.__cls

        def setnum(self, num):    # 국어점수 등수를 위해 번호를 num메소드로 정의 및 반환합니다.
            self.__num = num

        def getnum(self):
            return self.__num

        def setkr(self, kr):    # 국어점수 등수를 위해 국어점수를 kr메소드로 정의 및 반환합니다.
            self.__kr = kr

        def getkr(self):
            return self.__kr

        def set_st_num(self):    # 국어점수 등수를 위해 학번을 생성하는 함수입니다.
            self.__st_num = self.__year + '{:02}'.format(self.__cls) + '{:02}'.format(self.__num)
            return self.__st_num

    class Student_en:     # 영어점수 순 정렬을 위한 중첩클래스 입니다.
        def __init__(self,name,year,cls,num,en):
            self.__name = name
            self.__year = year
            self.__cls = cls
            self.__num = num
            self.set_st_num()
            self.__en = en

        def setname(self, name):    # 영어점수 등수를 위해 이름을 nm메소드로 정의 및 반환합니다.
            self.__name = name

        def getname(self):
            return self.__name

        def setyear(self, year):    # 영어점수 등수를 위해 학년을 year메소드로 정의 및 반환합니다.
            self.__year = year

        def getyear(self):
            return self.__year

        def setcls(self, cls):    # 영어점수 등수를 위해 반을 cls메소드로 정의 및 반환합니다.
            self.__cls = cls

        def getcls(self):
            return self.__cls

        def setnum(self, num):    # 영어점수 등수를 위해 번호를 num메소드로 정의 및 반환합니다.
            self.__num = num

        def getnum(self):
            return self.__num

        def seten(self, en):    # 영어점수 등수를 위해 영어점수를 en메소드로 정의 및 반환합니다.
            self.__en = en

        def geten(self):
            return self.__en

        def set_st_num(self):    # 영어점수 등수를 위해 학번을 생성하는 메소드입니다.
            self.__st_num = self.__year + '{:02}'.format(self.__cls) + '{:02}'.format(self.__num)
            return self.__st_num

    class Student_ma:     # 수학점수 순 정렬을 위한 중첩클래스 입니다.
        def __init__(self,name,year,cls,num,ma):
            self.__name = name
            self.__year = year
            self.__cls = cls
            self.__num = num
            self.set_st_num()
            self.__ma = ma

        def setname(self, name):    # 수학점수 등수를 위해 이름을 name메소드로 정의 및 반환합니다.
            self.__name = name

        def getname(self):
            return self.__name

        def setyear(self, year):    # 수학점수 등수를 위해 학년을 year메소드로 정의 및 반환합니다.
            self.__year = year

        def getyear(self):
            return self.__year

        def setcls(self, cls):    # 수학점수 등수를 위해 반을 cls메소드로 정의 및 반환합니다.
            self.__cls = cls

        def getcls(self):
            return self.__cls

        def setnum(self, num):    # 수학점수 등수를 위해 번호를 num메소드로 정의 및 반환합니다.
            self.__num = num

        def getnum(self):
            return self.__num

        def setma(self, ma):    # 수학점수 등수를 위해 수학점수를 ma메소드로 정의 및 반환합니다.
            self.__ma = ma

        def getma(self):
            return self.__ma

        def set_st_num(self):    # 수학점수 등수를 위해 학번을 생성하는 메소드입니다.
            self.__st_num = self.__year + '{:02}'.format(self.__cls) + '{:02}'.format(self.__num)
            return self.__st_num

print("===============================================")
print("성적 처리 프로그램에 오신 것을 환영합니다.")
print("처리할 학생 수는 총 4명입니다.")
print()
print("프로그램 진행 순서는")
print()
print("1. 4명의 학생 정보 입력.")
print("2. 전체 학생 목록 출력.")
print("3. 학생 별 총점 및 평균 출력.")
print("4. 이름 순 정렬.")
print("5. 총점 등수 출력.")
print("6. 국어 성적 등수 출력.")
print("7. 영어 성적 등수 출력.")
print("8. 수학 성적 등수 출력.")
print()
print("순으로 진행됩니다.")
print()
print("1. 먼저 4명의 학생 정보를 각각 입력해주시기 바랍니다.")
print("===============================================")
print()
print()
print("============ 첫 번째 학생 정보 입력 ============")        # 4명의 학생 정보를 입력받는 함수입니다.
Student1_name = input("첫 번째 학생 이름:")
Student1_year = input("{} 학생 학년:".format(Student1_name))        # 편의성을 위해 이름을 입력한 후로는 .
Student1_cls = int(input("{} 학생 반:".format(Student1_name)))     # 이름 이후의 정보 입력부터는 이름이 도출됩니다
Student1_num = int(input("{} 학생 번호:".format(Student1_name)))    # ex) "홍길동" 학생 학년, "홍길동" 학생 반 등등
Student1_kr = int(input("{} 학생 국어점수:".format(Student1_name)))
Student1_en = int(input("{} 학생 영어점수:".format(Student1_name)))
Student1_ma = int(input("{} 학생 수학점수:".format(Student1_name)))
print("======== 첫 번째 학생 정보 입력 완료 ! ========")
print()
print()
print("============ 두 번째 학생 정보 입력 ============")
Student2_name = input("두 번째 학생 이름:")
Student2_year = input("{} 학생 학년:".format(Student2_name))
Student2_cls = int(input("{} 학생 반:".format(Student2_name)))
Student2_num = int(input("{} 학생 번호:".format(Student2_name)))
Student2_kr = int(input("{} 학생 국어점수:".format(Student2_name)))
Student2_en = int(input("{} 학생 영어점수:".format(Student2_name)))
Student2_ma = int(input("{} 학생 수학점수:".format(Student2_name)))
print("======== 두 번째 학생 정보 입력 완료 ! ========")
print()
print()
print("============ 세 번째 학생 정보 입력 ============")
Student3_name = input("세 번째 학생 이름:")
Student3_year = input("{} 학생 학년:".format(Student3_name))
Student3_cls = int(input("{} 학생 반:".format(Student3_name)))
Student3_num = int(input("{} 학생 번호:".format(Student3_name)))
Student3_kr = int(input("{} 학생 국어점수:".format(Student3_name)))
Student3_en = int(input("{} 학생 영어점수:".format(Student3_name)))
Student3_ma = int(input("{} 학생 수학점수:".format(Student3_name)))
print("======== 세 번째 학생 정보 입력 완료 ! ========")
print()
print()
print("============ 네 번째 학생 정보 입력 ============")
Student4_name = input("네 번째 학생 이름:")
Student4_year = input("{} 학생 학년:".format(Student4_name))
Student4_cls = int(input("{} 학생 반:".format(Student4_name)))
Student4_num = int(input("{} 학생 번호:".format(Student4_name)))
Student4_kr = int(input("{} 학생 국어점수:".format(Student4_name)))
Student4_en = int(input("{} 학생 영어점수:".format(Student4_name)))
Student4_ma = int(input("{} 학생 수학점수:".format(Student4_name)))
print("======== 네 번째 학생 정보 입력 완료 ! ========")
print("모든 학생의 정보가 입력되었습니다!")
print()
print()

# 4명의 정보를 Student 클래스에 대입하여 학생 정보로 정의합니다.
# 정보 순서는 이름, (년도, 반, 번호) -> 학번으로 통합, 국어 점수, 영어 점수, 수학 점수 입니다.
Student1= Student(Student1_name, Student1_year, Student1_cls, Student1_num, Student1_kr, Student1_en, Student1_ma)
Student2= Student(Student2_name, Student2_year, Student2_cls, Student2_num, Student2_kr, Student2_en, Student2_ma)
Student3= Student(Student3_name, Student3_year, Student3_cls, Student3_num, Student3_kr, Student3_en, Student3_ma)
Student4= Student(Student4_name, Student4_year, Student4_cls, Student4_num, Student4_kr, Student4_en, Student4_ma)

# 정렬과 각 점수별 순위를 위해 학생 4명의 정보를 사전에 정의한 중첩 클래스에 대입하여 정의합니다.

# 이름 순 정렬을 위해 4명의 정보를 Student_name 클래스에 대입하여 학생 정보로 정의합니다.
# 또한 직접 접근을 위해 사전에 정의한 get 함수를 사용했습니다.
# 정보 순서는 이름, (년도, 반, 번호) -> 학번으로 통합, 국어 점수, 영어 점수, 수학 점수 입니다.
# 순위 매기기 작업을 위해 해당 정보들을 리스트에 포함시켰습니다.

Student1_sort_by_name = Student.Student_name(Student1.getname(),Student1.getyear(), Student1.getcls(), Student1.getnum())

Student2_sort_by_name = Student.Student_name(Student2.getname(),Student2.getyear(), Student2.getcls(), Student2.getnum())

Student3_sort_by_name = Student.Student_name(Student3.getname(),Student3.getyear(), Student3.getcls(), Student3.getnum())

Student4_sort_by_name = Student.Student_name(Student4.getname(),Student4.getyear(), Student4.getcls(), Student4.getnum())

Students_sort_by_name = [Student1_sort_by_name, Student2_sort_by_name, Student3_sort_by_name, Student4_sort_by_name]

# 총점 순 정렬을 위해 4명의 정보를 Student_total 클래스에 대입하여 학생 정보로 정의합니다.
# 또한 직접 접근을 위해 사전에 정의한 get 함수를 사용했습니다.
# 정보 순서는 이름, (년도, 반, 번호) -> 학번으로 통합, (국어 점수, 영어 점수, 수학 점수) -> 총점과 평균으로 통합입니다.
# 순위 매기기 작업을 위해 해당 정보들을 리스트에 포함시켰습니다.

Student1_sort_by_total = Student.Student_total(Student1.getname(),Student1.getyear(), Student1.getcls(),
                                               Student1.getnum(), Student1.getkr(), Student1.geten(), Student1.getma())

Student2_sort_by_total = Student.Student_total(Student2.getname(),Student2.getyear(), Student2.getcls(),
                                               Student2.getnum(), Student2.getkr(), Student2.geten(), Student2.getma())

Student3_sort_by_total = Student.Student_total(Student3.getname(),Student3.getyear(), Student3.getcls(),
                                               Student3.getnum(), Student2.getkr(), Student3.geten(), Student3.getma())

Student4_sort_by_total = Student.Student_total(Student4.getname(),Student4.getyear(), Student4.getcls(),
                                               Student4.getnum(), Student2.getkr(), Student4.geten(), Student4.getma())

Students_sort_by_total = [Student1_sort_by_total, Student2_sort_by_total, Student3_sort_by_total, Student4_sort_by_total]

# 국어 점수 순위를 위해 4명의 정보를 Student_kr 클래스에 대입하여 학생 정보로 정의합니다.
# 또한 직접 접근을 위해 사전에 정의한 get 함수를 사용했습니다.
# 정보 순서는 이름, (년도, 반, 번호) -> 학번으로 통합, 국어 점수입니다.
# 순위 매기기 작업을 위해 해당 정보들을 리스트에 포함시켰습니다.

Student1_sort_by_kr = Student.Student_kr(Student1.getname(),Student1.getyear(), Student1.getcls(), Student1.getnum(),
                                         Student1.getkr())

Student2_sort_by_kr = Student.Student_kr(Student2.getname(),Student2.getyear(), Student2.getcls(), Student2.getnum(),
                                         Student2.getkr())

Student3_sort_by_kr = Student.Student_kr(Student3.getname(),Student3.getyear(), Student3.getcls(), Student3.getnum(),
                                         Student3.getkr())

Student4_sort_by_kr = Student.Student_kr(Student4.getname(),Student4.getyear(), Student4.getcls(), Student4.getnum(),
                                         Student4.getkr())

Students_sort_by_kr = [Student1_sort_by_kr, Student2_sort_by_kr, Student3_sort_by_kr, Student4_sort_by_kr]

# 영어 점수 순위를 위해 4명의 정보를 Student_en 클래스에 대입하여 학생 정보로 정의합니다.
# 또한 직접 접근을 위해 사전에 정의한 get 함수를 사용했습니다.
# 정보 순서는 이름, (년도, 반, 번호) -> 학번으로 통합, 영어 점수입니다.
# 순위 매기기 작업을 위해 해당 정보들을 리스트에 포함시켰습니다.

Student1_sort_by_en = Student.Student_en(Student1.getname(),Student1.getyear(), Student1.getcls(), Student1.getnum(),
                                         Student1.geten())

Student2_sort_by_en = Student.Student_en(Student2.getname(),Student2.getyear(), Student2.getcls(), Student2.getnum(),
                                         Student2.geten())

Student3_sort_by_en = Student.Student_en(Student3.getname(),Student3.getyear(), Student3.getcls(), Student3.getnum(),
                                         Student3.geten())

Student4_sort_by_en = Student.Student_en(Student4.getname(),Student4.getyear(), Student4.getcls(), Student4.getnum(),
                                         Student4.geten())

Students_sort_by_en = [Student1_sort_by_en, Student2_sort_by_en, Student3_sort_by_en, Student4_sort_by_en]

# 수학 점수 순위를 위해 4명의 정보를 Student_ma 클래스에 대입하여 학생 정보로 정의합니다.
# 또한 직접 접근을 위해 사전에 정의한 get 함수를 사용했습니다.
# 정보 순서는 이름, (년도, 반, 번호) -> 학번으로 통합, 수학 점수입니다.
# 순위 매기기 작업을 위해 해당 정보들을 리스트에 포함시켰습니다.

Student1_sort_by_ma = Student.Student_ma(Student1.getname(),Student1.getyear(), Student1.getcls(), Student1.getnum(),
                                         Student1.getma())

Student2_sort_by_ma = Student.Student_ma(Student2.getname(),Student2.getyear(), Student2.getcls(), Student2.getnum(),
                                         Student2.getma())

Student3_sort_by_ma = Student.Student_ma(Student3.getname(),Student3.getyear(), Student3.getcls(), Student3.getnum(),
                                         Student3.getma())

Student4_sort_by_ma = Student.Student_ma(Student4.getname(),Student4.getyear(), Student4.getcls(), Student4.getnum(),
                                         Student4.getma())

Students_sort_by_ma = [Student1_sort_by_ma, Student2_sort_by_ma, Student3_sort_by_ma, Student4_sort_by_ma]

def sortstudents_name(Student):     # 오브젝트를 이름으로 정렬하기 위한 함수입니다.
    return Student.getname()

def sortstudents_total(Student):     # 오브젝트를 총점으로 정렬하기 위한 함수입니다. 총점 순위 구하기에 활용됩니다.
    return Student.get_total()

def sortstudents_kr(Student):     # 오브젝트를 국어점수로 정렬하기 위한 함수입니다. 국어점수 순위 구하기에 활용됩니다.
    return Student.getkr()

def sortstudents_en(Student):     # 오브젝트를 영어점수로 정렬하기 위한 함수입니다. 영어점수 순위 구하기에 활용됩니다.
    return Student.geten()


def sortstudents_ma(Student):     # 오브젝트를 수학점수로 정렬하기 위한 함수입니다. 수학점수 순위 구하기에 활용됩니다
    return Student.getma()


print("====================================== 2. 전체 학생 목록 ======================================")
Student1.print_student()    # Student 클래스 안에 있는 print_student를 통해 전체 학생 목록을 출력합니다.
Student2.print_student()
Student3.print_student()
Student4.print_student()
print("===============================================================================================")
print()
print()
print("============== 3. 학생 별 총점 및 평균 =============")
Student1.print_total_avg()      # Student 클래스 안에 있는 print_total_avg를 통해 학생 별 총점과 평균을 출력합니다.
Student2.print_total_avg()
Student3.print_total_avg()
Student4.print_total_avg()
print("====================================================")
print()
print()

print("====== 4. 이름순 정렬 ======")  # 반복문과 sort 그리고 sortstudents_name를 활용하여 이름 순 정렬을 구합니다.
sorted_students_name= sorted(Students_sort_by_name, key= sortstudents_name)
for i in range(Student.Num_of_Students):
    print("이름 : {} / 학번 : {}"
          .format(sorted_students_name[i].getname(), sorted_students_name[i].set_st_num()))
print("============================")

print()
print()

print("======================= 5. 총점 등수 =======================")  # 반복문과 sort 그리고 sortstudents_total을 활용하여
                                                                        # 총점 등수를 구합니다.
sorted_students_total= sorted(Students_sort_by_total, key= sortstudents_total,reverse = True)
for i in range(Student.Num_of_Students):
    print("{}등 : {}점 / 평균 : {}점. (이름 : {} / 학번 : {})" \
        .format(i + 1, sorted_students_total[i].get_total(), sorted_students_total[i].get_avg(),
                sorted_students_total[i].getname(), sorted_students_total[i].set_st_num()))
print("============================================================")

print()
print()

print("============ 6. 국어 성적 등수 ============")  # 반복문과 sort 그리고 sortstudents_kr을 활용하여 국어성적 등수를 구합니다.
sorted_students_kr= sorted(Students_sort_by_kr, key= sortstudents_kr,reverse = True)
for i in range(Student.Num_of_Students):
    print("{}등 : {}점. (이름 : {} / 학번 : {})" \
        .format(i + 1, sorted_students_kr[i].getkr(), sorted_students_kr[i].getname(), sorted_students_kr[i].set_st_num()))
print("===========================================")

print()
print()

print("============ 7. 영어 성적 등수 ============")  # 반복문과 sort 그리고 sortstudents_en을 활용하여 영어성적 등수를 구합니다.
sorted_students_en= sorted(Students_sort_by_en, key= sortstudents_en, reverse = True)
for i in range(Student.Num_of_Students):
    print("{}등 : {}점. (이름 : {} / 학번 : {})" \
        .format(i + 1, sorted_students_en[i].geten(), sorted_students_en[i].getname(), sorted_students_en[i].set_st_num()))
print("===========================================")

print()
print()

print("============ 8. 수학 성적 등수 ============")  # 반복문과 sort 그리고 sortstudents_ma을 활용하여 수학성적 등수를 구합니다.
sorted_students_ma= sorted(Students_sort_by_ma, key= sortstudents_ma, reverse = True)
for i in range(Student.Num_of_Students):
    print("{}등 : {}점. (이름 : {} / 학번 : {})" \
        .format(i + 1, sorted_students_ma[i].getma(), sorted_students_ma[i].getname(), sorted_students_ma[i].set_st_num()))
print("===========================================")

print()
print()

print("===================================================")
print("===============처리가 완료되었습니다!==============")
print("===================================================")