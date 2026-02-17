# 두 수의 나눗셈
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120806
# 알고리즘: 기초
# 작성자: 김혜수
# 작성일: 2026. 02. 17. 18:23:06

def solution(num1, num2):
    answer = (num1/num2)*1000
    return int(answer)


# 나눈 값을 정수로 return해야 하니까 int() 형변환 필수