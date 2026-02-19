# 중앙값 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120811
# 알고리즘: 기초
# 작성자: 김혜수
# 작성일: 2026. 02. 19. 15:42:25

import statistics
             #이 자리는 어떠한 값을 넣어주는 곳?
def solution(array):
    median_value = statistics.median(array)
    return median_value #쓰기는 썼는데 이해가 완벽히 된 것 같진 않은....

    
#    answer = 0
#    return answer

#라이브러리가 있으면 라이브러리 활용해서 해도 되는 건지, 아니면 코드로 구현해 내야 하는 건지!?
