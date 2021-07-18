#### 상하좌우

# 입력 예시
# 5

#출력 예시
# 11475

#### 내 풀이 #####################
n = int(input())

count = 0
three = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53] # ㅋㅋㅋ 이건 좀;; 
for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            if second in three or minute in three or hour in three :
                count += 1

print(count)

#### 내 풀이2 ###################
n = int(input())

count = 0

for hour in range(n+1):
    for minute in range(60):
        for second in range(60):

            if second % 10 ==3 or second//10 == 3 or minute % 10 ==3 or minute//10 == 3 or hour % 10 ==3 or hour//10 == 3: # 흠..
                count += 1

print(count)

##################################
# 나동빈 풀이1 ###############
h = int(input)

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k): # 이런 방법이 ㅋㅋㅋ
                count += 1
    
print(count)