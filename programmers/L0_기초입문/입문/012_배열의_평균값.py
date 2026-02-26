# 배열의 평균값
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 알고리즘: 기초
# 작성자: 김혜수
# 작성일: 2026. 02. 26. 11:50:58

'''
import numpy as np

def solution(numbers):
    answer = np.mean(numbers)
    return answer
'''
def solution(numbers):
    return sum(numbers)/len(numbers)