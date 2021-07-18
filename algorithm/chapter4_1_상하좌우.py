#### 상하좌우

# 입력 예시
# 5
# R R R U D D

#출력 예시
# 3 4

#### 내 풀이 #####################

n = int(input())
move = input().split()
position = [1,1] 
for i in move:
    if i == 'R' and position[1] != n:
        position[1] += 1
    elif i =='L'and position[1] != 1:
        position[1] -= 1
    elif i == 'U'and position[0] != 1:
        position[0] -= 1
    elif i == 'D'and position[0] != n:  
        position[0] += 1


print(position[0], position[1])

##############################
# 나동빈 풀이1 ############
n = int(input())

x, y = 1, 1
plans = input().split()

dx = [0,0,-1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny

print(x, y)

