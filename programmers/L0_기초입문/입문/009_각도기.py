# 각도기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 알고리즘: 기초
# 작성자: 김혜수
# 작성일: 2026. 02. 20. 12:37:59

def solution(angle):
    if angle < 90 :
        return 1
    elif angle == 90:
        return 2
    elif angle < 180:
        return 3
    elif angle == 180:
        return 4

#    answer = 0
#    return answer