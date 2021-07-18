#### 왕실의 나이트

# 입력 예시
# a1

#출력 예시
# 2
#### 내 풀이 #####################

p = list(input())
p =[ord(p[0]), int(p[1])]

count = 0

#경우의 수 8개
if p[0] + 2 < ord('h') and p[1] + 1 < 9:
    count +=1
if p[0] + 2 < ord('h') and p[1] - 1 > 0:
    count +=1
if p[0] - 2 >= ord('a') and p[1] + 1 < 9:
    count +=1
if p[0] - 2 >= ord('a') and p[1] - 1 > 0:
    count +=1
if p[0] + 1 < ord('h') and p[1] + 2 < 9:
    count +=1
if p[0] - 1 >= ord('a') and p[1] + 2 < 9:
    count +=1
if p[0] + 1 < ord('h') and p[1] - 2 > 0:
    count +=1
if p[0] - 1 >= ord('a') and p[1] - 2 > 0:
    count +=1

print(count)

####################################
# 나동빈 풀이 1 ########

input_data = input()
row = int(input_data[1])
column = int(ord[inpt_data[0]]) - int(ord('a'))  + 1

steps = [(-2, -1), {-1, -2}, (1, -2), (2,-1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

rasult = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_row <=8 and next_column <= 8:
        result += 1

print(result)