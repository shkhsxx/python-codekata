# 중앙값 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120811
# 알고리즘: 기초
# 작성자: 김혜수
# 작성일: 2026. 02. 23. 15:19:31

import statistics
             #이 자리는 어떠한 값을 넣어주는 곳?
def solution(array):
    median_value = statistics.median(array)
    return median_value 

    
#    answer = 0
#    return answer
