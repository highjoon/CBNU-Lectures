
itemPrice=int(input("물건값을 입력하시오."))
note50000=int(input("50000원 지폐개수."))
note10000=int(input("10000원 지폐개수."))
note5000=int(input("5000원 지폐개수."))
note1000=int(input("1000원 지폐개수."))
coin500=int(input("500원 동전개수."))
coin100=int(input("100원 동전개수."))
coin50=int(input("50원 동전개수."))
coin10=int(input("10원 동전개수."))
coin5=int(input("5원 동전개수."))
coin1=int(input("1원 동전개수."))

change=note50000*50000+note10000*10000+note5000*5000+note1000*1000+coin500*500+coin100*100+coin50*50+coin10*10+coin5*5+coin1*1-itemPrice

#거스름돈(50000원 지폐 개수)을 계산한다.
nNote50000=change//50000
change=change%50000

#거스름돈(10000원 지폐 개수)을 계산한다.
nNote10000=change//10000
change=change%10000

#거스름돈(5000원 지폐 개수)을 계산한다.
nNote5000=change//5000
change=change%5000

#거스름돈(1000원 지폐 개수)을 계산한다.
nNote1000=change//1000
change=change%1000

#거스름돈(500원 동전 개수)을 계산한다.
nCoin500=change//500
change=change%500

#거스름돈(100원 동전 개수)을 계산한다.
nCoin100=change//100
change=change%100

#거스름돈(50원 동전 개수)을 계산한다.
nCoin50=change//50
change=change%50

#거스름돈(10원 동전 개수)을 계산한다.
nCoin10=change//10
change=change%10

#거스름돈(5원 동전 개수)을 계산한다.
nCoin5=change//5
change=change%5

#거스름돈(1원 동전 개수)을 계산한다.
nCoin1=change

print("50000원=", nNote50000, "장", "10000원=", nNote10000, "장", "5000원=", nNote5000,"장", "1000원=", nNote1000,"장", "500원=", nCoin500,"개", "100원=", nCoin100,"개", "50원=", nCoin50,"개", "10원=", nCoin10,"개", "5원=", nCoin5,"개", "1원=", nCoin1,"개")
