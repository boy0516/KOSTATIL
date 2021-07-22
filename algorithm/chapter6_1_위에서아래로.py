#### 위에서 아래로

# 입력 예시
# 3
# 15
# 27
# 12

# 출력 예시
# 27 15 12

#### 내 풀이 #####################

n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))

num_list = sorted(num_list, reverse=True)

for i in num_list:
    print(i, end=" ")

#################################
# 나동빈 풀이 ######

# N을 입력받기
n = int(input())

# N개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array, reverse=True)

for i in array:
    print(i, end=" ")