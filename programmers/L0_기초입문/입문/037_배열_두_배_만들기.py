# 배열 두 배 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120809
# 알고리즘: 기초
# 작성자: 김혜수
# 작성일: 2026. 02. 24. 08:52:32

def solution(numbers):
    result = []
    
    for num in numbers:
        result.append(num*2)
    return result
    
    
#    answer = []
#    return answer

# for문으로 구현해보기
"""

arr = [1,2,3] #[2, 4, 6]
result = []

for num in arr : 
  #print(f"지금 num의 값 : {num}, 그러므로 num*2={num*2}")
  result.append(num*2)
  #print(f"append 이후 result 배열 => {result}")
 
 """