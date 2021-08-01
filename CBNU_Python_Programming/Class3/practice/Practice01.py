"""
실습 1) 이름 추출하기

다음과 같은 문자열을 변수 data에 저장하여 이중 이름만 출력하여라.
data = '정보통계학과,2025016***,강도영,val***@naver.com'

출력
강도영
"""
data = '정보통계학과,2025016***,강도영,val***@naver.com'

li = data.split(',')
print(li[2])