#### 1이 될 때까지

# 입력 예시
# 25 5

#출력 예시
# 2

#### 내 풀이 #####################

N, M = map(int, input().split())

count = 0

while True :  
    
    for i in range(N%M): # M의 배수까지 1씩 빼주는 반복문
        N -= 1
        count += 1
        if N == 1:
            break
    if N == 1:
        break

    N = int(N/M) # M으로 나누어줌
    count += 1
    if N == 1:
        break
    
    print(N)

print(count)

#####################################
# 나동빈 풀이1 ###########

n, k = map(int, input().split())
result = 0

# N이 K이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n - = 1
        result += 1
    
    n //= K
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)


#####################################
# 나동빈 풀이2 ########

n, k = map(int, input().split())
result = 0

while True:
    # (N==K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n//k)*k
    result += (n - target)
    n = target

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    result += 1

    n //= k

# 마지막으로 남은 수에 대하여 1씩 뺴기
result += (n-1)
print(result)

