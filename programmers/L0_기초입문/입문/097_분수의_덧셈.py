# 분수의 덧셈
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120808
# 알고리즘: 기초
# 작성자: 김혜수
# 작성일: 2026. 02. 19. 15:11:24

import math

def solution(numer1, denom1, numer2, denom2):
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2 #통분
    gcd_value = math.gcd(numer, denom) #최대공약수 라이브러리 사용
    return numer // gcd_value, denom // gcd_value #분자,분모를 최대공약수로 나눠주면 기약분수!


# 두 분수를 더한 값:
# 1-1: 분모를 같게 해준다(다른 분수의 분모와 같게 분자와 분모에 2를 곱한다)
# 1-2: 분자끼리 더한다
# 2: 기약분수로 표현한다
# 2-2: 최대공약수로 분모와 분자를 나누기(외부 라이브러리)
# import math 
# math.gcd(숫자1, 숫자2) :
# 숫자 1이랑 2의 최대공약수를 구해줌
# 3: 기약분수의 분자와 분모의 배열을 바꿔서 return 해준다
