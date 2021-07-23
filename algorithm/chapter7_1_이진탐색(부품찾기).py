#### 부품찾기

#입력예시
# 5
# 8 3 7 9 2
# 3
# 5 7 9

# 출력예시
# no yes yes

#### 내 풀이 #####################

N = int(input())

goods = list(map(int, input().split()))
goods.sort() ########################################## 이진탐색을 위해 반드시 정렬을 해줘야함
print(goods)
M = int(input())

order = list(map(int, input().split()))
print(order)

#시작점과 끝점
start = 0
end = N-1

# 이진 탐색
def binary_search(target, start, end):
    if start>end:
        return "no"
        
    mid = (start + end) // 2
    
    if goods[mid]==target:
        return "yes"
    
    elif goods[mid]>target:
        return binary_search(target, start, mid-1)
    
    elif goods[mid]<target:
        return binary_search(target, mid+1, end)
    
# 타겟값을 바꿔가며 이진탐색 진행
for target in order:
    print(binary_search(target, start, end), end=" ")

#################################################
#################################################
# 나동빈 풀이 1#######

# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid -1

        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
        return None

n = int(input())

#물품 입력
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행

m = int(input())
x = list(map(int, input().split())) # 요청

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=" ")
    else:
        print('no', end = " ")


