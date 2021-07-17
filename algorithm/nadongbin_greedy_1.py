#### 큰 수의 법칙

# 입력 예시
# 5 8 3
# 2 4 5 4 6

#### 내 풀이 #####################

N, M, K = map(int, input().split()) # N=5, M=8, K=3

#리스트 형태로 받아준다.  numbers = ['2','4','5','4','6']
numbers = input().split()

# 가장 두 수
num1 = 0
num2 = 0

# 반환 값(큰 수의 합)
answer = 0

for i in numbers: 
    j = int(i) # 문자를 정수로 형변환

    if j >= num1 or j >= num2: #num1이나 num2보다 크다면 num1과 num2 중 작은 변수에 저장
        if num1>=num2:
            num2 = j
        else:
            num1 = j

# K번 마다 작은 수를 더해줘야 하므로 answer에 
# 가장 큰수를 M-M%K번 더해주고 
# 두번째 큰 수를 M%K번 더해준다.
num3 = int(M/(K+1))
if num1 >= num2: 
    answer += num1*(M-num3)
    answer += num2*num3
else:
    answer += num2*(M-num3)
    answer += num1*num3

print(answer) # 반환값 46




############################################
#### 나동빈 풀이 1###################
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰수

result = 0

while True:
    for i in rnage(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기

    if m == 0: # m=0이라면 반복문 탈출
        break

    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 #더할 때마다 1씩 빼기

print(result) #출력




#### 나동빈 풀이 2###################
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k + 1) # 짜투리 개수

result = 0
result += (count) * first
result += (m -count) * second # 두 번째로 큰 수 더하기

print(result)