# 두 수의 나눗셈
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120806
# 알고리즘: 기초
# 작성자: 김혜수
# 작성일: 2026. 02. 17. 18:18:26

def solution(num1, num2):
    answer = (num1/num2)*1000
    return int(answer)


# 나눗셈 후 나머지 값은 버리고 몫만 남겨서 X1000을 해야 할 것 같은데...