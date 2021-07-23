#### 떡볶이 떡 만들기

# 입력예시
# 4 6
# 19 15 10 17

# 출력예시
# 15

#### 내 풀이 #####################
n, m = map(int, input().split())

DDuck = list(map(int, input().split()))
DDuck.sort()

cutting = 0
mid = 0
for i in range(DDuck):
    cutting += DDuck[i]-min(DDuck)
    

if m == cutting:
    print(cutting)
elif m > cutting:
    print(m)