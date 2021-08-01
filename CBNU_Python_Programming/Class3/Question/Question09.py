"""
사용자로부터 두 개의 문자열을 입력받아 공통으로 두 문자열에서
공통으로 있는 문자들을 콤마(,)로 구분하여 출력하는 코드를 작성하시오.
"""

a = input("문자열 1 : ")
b = input("문자열 2 : ")

s1 = set(a)
s2 = set(b)

common = s1 & s2
# & 또는 intersection : 교집합
print(','.join(common))
