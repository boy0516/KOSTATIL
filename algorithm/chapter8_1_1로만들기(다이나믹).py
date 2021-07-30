#### 1로 만들기

# 입력예시
# 26

# 출력예시
# 3

#### 내 풀이 #####################

## 문제점.. 다이나믹 프로그래밍을 하지 않아서 모든 경우를 전부 탐색한다. 
# 수가 500 정도만 넘어가도 실행시간이 매우 걸어짐.
# n^4*(1/30)번 연산을 진행 
# O(n^4) 아래꺼 나동빈 코드는 O(n)
n = int(input())
arr = [] # 계산횟수 담아놓은

def calculater(n, count):
    count += 1
    if n == 1:
        arr.append(count-1)
        return

    if n % 5 == 0:
        calculater(n/5,count)

    if n% 3 == 0:
        calculater(n/3,count)

    if n % 2 == 0:
        calculater(n/2,count)

    calculater(n-1,count)
    
calculater(n,0)

print(min(arr))

##################################
# 나동빈 풀이 #####

# 정수 X를 입력받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
for i in range(2 , x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] +1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] +1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])

# 와... 직접해보니까 확 다르긴 함..