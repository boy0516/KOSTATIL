#### 숫자 카드 게임

# 입력 예시
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

#### 내 풀이 #####################

N, M = map(int, input().split())

low_list = [] # 각 행의 최소값을 저장하는 리스트

for i in range(N):
    numbers = list(map(int,input().split())) # 각 행의 입력을 리스트로 받음
    
    low_num = numbers[0] # 값 초기화

    for j in numbers: # 행의 최소값을 찾는 반복문
        if low_num > j:
            low_num = j
    low_list.append(low_num) # 최소값을 리스트에 저장

result = 0
for i in low_list: # 각 행의 최소값을 비교해 그 중 가장 큰 값을 찾음
    if result < i:
        result = i

print(result)
        
#######################
# 나동빈 풀이1#############

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = 10001
    for a in data:
        min_value = min(min_value,a)
    
    result = max(result, min_value)

print(result)

###########################
# 나동빈 풀이2####################
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)