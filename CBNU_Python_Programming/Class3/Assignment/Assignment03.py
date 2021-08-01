import math

def SimpleInterest(principal, interestRate, period):
    rate = float(interestRate / 100)
    simple = math.floor(principal * rate * period)

    print("{0}년 후 단리 이자는 {1}원입니다.".format(period, simple))

def CompoundInterest(principal, interestRate, period):
    rate = float(interestRate / 100)
    compound = math.floor((principal * (1 + rate) ** period) - principal)

    print("{0}년 후 복리 이자는 {1}원입니다.".format(period, compound))

def main():
    principal = int(input("원금을 입력하세요 : "))
    interestRate = int((input("연이자율을 입력하세요 : ")))
    period = int(input("예치기간을 입력하세요 : "))

    print()

    print("원금(원) : {0}".format(principal))
    print("이자율(%) : {0}".format(interestRate))
    print("예치기간(년) : {0}".format(period))

    print()

    SimpleInterest(principal, interestRate, period)
    CompoundInterest(principal, interestRate, period)

if __name__ == '__main__':
    main()

