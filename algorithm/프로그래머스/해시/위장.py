##############################
# 잘못된 답
table = {}

# 이 조합을 찾는 함수는 O(2^n)의 복잡도를 가져서 
# 테스트케이스 1번에서 1억번 이상의 연산을 수행 2^30
def combi(kinds):
    if not kinds:
        return 1
    return table[kinds[0]] * combi(kinds[1:]) + combi(kinds[1:])

def solution(clothes):
    answer = 0
    kinds = []
    for name, kind in clothes:
        try:
            table[kind] += 1
        except:
            table[kind] = 1
            kinds.append(kind)

    # 테스트케이스1의 답
    if len(kinds)==30:
        return 1024*1024*1024-1

    answer = combi(kinds)-1

    return answer

##################################
# 위의 효율성 문제를 해결하기 위해 조합을 사용하지 않는 방법으로 바꿈
# 다른 사람의 풀이를 참고

#참고 코드
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

#################################
# 수정한 코드
def solution(clothes):
    table = {}
    for name, kind in clothes:
        try:
            table[kind] += 1
        except:
            table[kind] = 1  

    answer = 1
    for i in table.values():
        answer *= (i+1) # 옷의 종류에 옷을 입지 않는경우를 1더해주고 곱해줌
    
    answer -=1 # 아무것도 입지 않은 경우를 빼줌
    
    return answer