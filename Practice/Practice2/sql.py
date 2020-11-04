import sqlite3

con = sqlite3.connect("testDB")
cur = con.cursor()


# 테이블 전체 조회
all_sql = "SELECT * FROM jejutourist"

# 월별 Individual, Package, Leisure 방문객 합계
Sum_individual_group_leisure_sql = "SELECT SUM(d_individual), SUM(d_package), SUM(d_leisure) AS dum_of_d_group FROM jejutourist;"

# 월별 Individual, Package, Leisure 방문객 3년치 합계
Sum_individual_group_leisure_month_sql = "SELECT month, SUM (d_individual), SUM (d_package), SUM (d_leisure) AS dum_of_d_package FROM jejutourist GROUP BY month ORDER BY month;"

# 월별 각 국가에서 입도한 관광객 수
Num_tourist_sql = "SELECT month, SUM(f_japan), SUM(f_china), SUM(f_hongkong), SUM(f_taiwan), SUM(f_singapore), SUM(f_malasia), SUM(f_indonesia), SUM(f_vietnam), SUM(f_thailand), SUM(f_usa) AS dum_of_d_group FROM jejutourist GROUP BY month ORDER BY month;"

all = con.execute(all_sql)

sum = con.execute(Sum_individual_group_leisure_sql)

sumMonth = con.execute(Sum_individual_group_leisure_month_sql)

NumTourist = con.execute(Num_tourist_sql)

for i in NumTourist:
    print (i)

con.commit()