#문과학생의 수능성적표를 작성하는 프로그램을 구현합니다.
#응시자의 인적사항은 수험번호, 이름, 생년월일, 성별, 출신고교를 입력합니다.
#응시과목은 국어, 영어, 수학, 탐구1, 탐구2 입니다.
#여러 학생들의 성적표를 작성하기 위해 while반복문을 이용합니다.

while 1:

#수험번호, 생년월일은 정수가 아닌 값을 입력하면 반복문을 멈춥니다.
    
    studentCode=int(input("수험번호"))
    if studentCode=="":
        break
    birth=int(input("생년월일"))
    if birth=="":
        break
    
#이름, 성별, 출신고교는 입력을 하지 않으면 반복문을 멈춥니다.
    
    name=str(input("이름"))
    if name =="":
        break        
    sex=str(input("성별"))
    if sex=="":
        break
    highSchool=str(input("출신고교"))
    if highSchool=="":
        break
    
#각 과목의 점수는 정수가 아닌 값을 입력하면 반복문을 멈춥니다.
    
    kScore=int(input("국어점수"))
    if kScore=="":
        break
    eScore=int(input("영어점수"))
    if eScore=="":
        break
    mScore=int(input("수학점수"))
    if mScore=="":
        break
    study1Score=int(input("탐구1점수"))
    if study1Score=="":
        break
    study2Score=int(input("탐구2점수"))
    if study2Score=="":
        break

#응시자의 인적사항은 별도로 표시합니다.
    
    print("==================================================================")
    print("수험번호 :",studentCode,"이름 :",name)
    print("생년월일 :",birth,"성별 :",sex)
    print("출신고교 :",highSchool)
    print("==================================================================")

#등급을 구분하는 기준은 절대등급으로 10점 단위당 1등급이며 백분위값은 실제 수능 성적에서의 비율을 적용하였습니다.
    
    if kScore>90:
        print("국어 성적 :",kScore,"점","1등급","상위4%이내입니다.")
    elif kScore>80:
        print("국어 성적 :",kScore,"점","2등급","상위11%이내입니다.")
    elif kScore>70:
        print("국어 성적 :",kScore,"점","3등급","상위23%이내입니다.")
    elif kScore>60:
        print("국어 성적 :",kScore,"점","4등급","상위40%이내입니다.")
    elif kScore>50:
        print("국어 성적 :",kScore,"점","5등급","상위60%이내입니다.")
    elif kScore>40:
        print("국어 성적 :",kScore,"점","6등급","상위77%이내입니다.") 
    elif kScore>30:
        print("국어 성적 :",kScore,"점","7등급","상위89%이내입니다.")
    elif kScore>20:
        print("국어 성적 :",kScore,"점","8등급","상위96%이내입니다.")
    else:
        print("국어 성적 :",kScore,"점","9등급","상위96%이하입니다.")

    
    if eScore>90:
        print("영어 성적 :",eScore,"점","1등급","상위4%이내입니다.")
    elif eScore>80:
        print("영어 성적 :",eScore,"점","2등급","상위11%이내입니다.")
    elif eScore>70:
        print("영어 성적 :",eScore,"점","3등급","상위23%이내입니다.")
    elif eScore>60:
        print("영어 성적 :",eScore,"점","4등급","상위40%이내입니다.")
    elif eScore>50:
        print("영어 성적 :",eScore,"점","5등급","상위60%이내입니다.")
    elif eScore>40:
        print("영어 성적 :",eScore,"점","6등급","상위77%이내입니다.") 
    elif eScore>30:
        print("영어 성적 :",eScore,"점","7등급","상위89%이내입니다.")
    elif eScore>20:
        print("영어 성적 :",eScore,"점","8등급","상위96%이내입니다.")
    else:
        print("영어 성적 :",eScore,"점","9등급","상위96%이하입니다.")

    if mScore>90:
        print("수학 성적 :",mScore,"점","1등급","상위4%이내입니다.")
    elif mScore>80:
        print("수학 성적 :",mScore,"점","2등급","상위11%이내입니다.")
    elif mScore>70:
        print("수학 성적 :",mScore,"점","3등급","상위23%이내입니다.")
    elif mScore>60:
        print("수학 성적 :",mScore,"점","4등급","상위40%이내입니다.")
    elif mScore>50:
        print("수학 성적 :",mScore,"점","5등급","상위60%이내입니다.")
    elif mScore>40:
        print("수학 성적 :",mScore,"점","6등급","상위77%이내입니다.") 
    elif mScore>30:
        print("수학 성적 :",mScore,"점","7등급","상위89%이내입니다.")
    elif mScore>20:
        print("수학 성적 :",mScore,"점","8등급","상위96%이내입니다.")
    else:
        print("수학 성적 :",mScore,"점","9등급","상위96%이하입니다.")

    if study1Score>45:
        print("탐구1 성적 :",study1Score,"점","1등급","상위4%이내입니다.")
    elif study1Score>40:
        print("탐구1 성적 :",study1Score,"점","2등급","상위11%이내입니다.")
    elif study1Score>35:
        print("탐구1 성적 :",study1Score,"점","3등급","상위23%이내입니다.")
    elif study1Score>30:
        print("탐구1 성적 :",study1Score,"점","4등급","상위40%이내입니다.")
    elif study1Score>25:
        print("탐구1 성적 :",study1Score,"점","5등급","상위60%이내입니다.")
    elif study1Score>20:
        print("탐구1 성적 :",study1Score,"점","6등급","상위77%이내입니다.") 
    elif study1Score>15:
        print("탐구1 성적 :",study1Score,"점","7등급","상위89%이내입니다.")
    elif study1Score>10:
        print("탐구1 성적 :",study1Score,"점","8등급","상위96%이내입니다.")
    else:
        print("탐구1 성적 :",study1Score,"점","9등급","상위96%이하입니다.")

    if study2Score>45:
        print("탐구2 성적 :",study2Score,"점","1등급","상위4%이내입니다.")
    elif study2Score>40:
        print("탐구2 성적 :",study2Score,"점","2등급","상위11%이내입니다.")
    elif study2Score>35:
        print("탐구2 성적 :",study2Score,"점","3등급","상위23%이내입니다.")
    elif study2Score>30:
        print("탐구2 성적 :",study2Score,"점","4등급","상위40%이내입니다.")
    elif study2Score>25:
        print("탐구2 성적 :",study2Score,"점","5등급","상위60%이내입니다.")
    elif study2Score>20:
        print("탐구2 성적 :",study2Score,"점","6등급","상위77%이내입니다.") 
    elif study2Score>15:
        print("탐구2 성적 :",study2Score,"점","7등급","상위89%이내입니다.")
    elif study2Score>10:
        print("탐구2 성적 :",study2Score,"점","8등급","상위96%이내입니다.")
    else:
        print("탐구2 성적 :",study2Score,"점","9등급","상위96%이하입니다.")
