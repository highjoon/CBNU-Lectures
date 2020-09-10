#계산할 연도와 월을 입력합니다.
year=int(input("연도를 입력하시오:"))
month=int(input("월을 입력하시오:"))

#사용자가 입력한 월이 해당하는 해가 윤년인지 계산합니다.
if((year%4==0 and year%100 !=0) or year%400==0):
    print(year, "년은 윤년입니다.")
else:
    print(year,"년은 윤년이 아닙니다.")

#2월을 입력했을 때 윤년이면 29일, 그렇지 않으면 28일을 출력합니다.
if(month==2):
    if(year%4==0 and year%100 !=0) or year%400==0:
        print("월의 날수는 29일입니다.")
    else:
        print("월의 날수는 28일입니다.")

#2월이 아닌 달 중 4,6,9,11월이면 30일, 그외 월을 입력하면 31일을 출력합니다.
elif(month==4 or month==6 or month==9 or month==11):
    print("월의 날수는 30일입니다.")
else:
    print(year,"년", month, "월의 날수는 31일입니다.")
    
