import sqlite3

con = sqlite3.connect("testDB.db")
cur = con.cursor()

# AS 구문은 테이블 또는 테이블의 열에 대해서 임시로 이름을 변경

# GROUP BY절
# 용도 : 일반적으로 특정 그룹(포지션별, 팀별)별 데이터를 필요로 할 경우에 GROUP BY절을  그룹함수와 함께 이용한다.
# GROUP BY절 이용시, SELECT에 지정한 칼럼은 GROUP BY절에 모두 포함해야 한다.

# ORDER BY절
# 조회된 결과의 데이터들을 정렬하여 보기 좋게 만들어준다.
# 기본적으로 ORDER BY는 오름차순 정렬이 되어 ASC 생략이 가능하다.
# 또한 모든 절을 다 이용한다면, 작성 순서는 다음과 같다.
# WHERE절->GROUP BY절->ORDER BY절

# 테이블 전체 조회
all_sql = "SELECT * FROM jejutourist"

# 월별 Individual, Package, Leisure 방문객 합계 (3년치 합계)
Sum_individual_package_leisure_sql = "SELECT month, \
                                                                        SUM(d_individual), \
                                                                        SUM(d_package), \
                                                                        SUM(d_leisure) \
                                                                        AS dum_of_d_group \
                                                                        FROM jejutourist;"

# 월별 Individual, Package, Leisure 방문객 3년치 합계
Sum_individual_package_leisure_month_sql = "SELECT month, \
                                                                                    SUM (d_individual), \
                                                                                    SUM (d_package), \
                                                                                    SUM (d_leisure) \
                                                                                    AS dum_of_d_package \
                                                                                    FROM jejutourist \
                                                                                    GROUP BY month \
                                                                                    ORDER BY month;"

# 월별 각 국가에서 입도한 관광객 수
Num_tourist_sql = "SELECT month, \
                                     SUM(f_japan), \
                                     SUM(f_china), \
                                     SUM(f_hongkong), \
                                     SUM(f_taiwan), \
                                     SUM(f_singapore), \
                                     SUM(f_malasia), \
                                     SUM(f_indonesia), \
                                     SUM(f_vietnam), \
                                     SUM(f_thailand), \
                                     SUM(f_usa) \
                                     AS dum_of_d_group \
                                     FROM jejutourist \
                                     GROUP BY month \
                                     ORDER BY month;"

all = con.execute(all_sql)

Sum_individual_package_leisure = con.execute(Sum_individual_package_leisure_sql)

Sum_individual_package_leisure_month = con.execute(Sum_individual_package_leisure_month_sql)

Num_tourist = con.execute(Num_tourist_sql)

for i in Sum_individual_package_leisure_month:
    print (i)

con.commit()