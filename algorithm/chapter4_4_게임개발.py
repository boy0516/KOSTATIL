#### 게임 개발

# 입력 예시
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

#출력 예시
# 3

#### 내 풀이 #####################
n, m = map(int,input().split())

# 현재 위치와 방향
state = list(map(int,input().split()))
# 지도를 담은 이차원리스트
map_list = []
#방문좌표를 저장하는 리스트
visits = []

for i in range(n):
    map_list.append(list(map(int,input().split())))

# 방향에 따른 좌표이동
move = [(0, -1), (1, 0), (0, 1), (-1, 0)]

count = 0
cannot_move = 0
while True:
    
    # 이동 예상좌표 계산과 방향 조정
    if state[2] != 0:
        nx = state[0] + move[state[2]-1][0]
        ny = state[1] + move[state[2]-1][1]
        state[2] -= 1
    else:
        nx = state[0] + move[3][0]
        ny = state[1] + move[3][1]
        state[2] = 3
    
    # 예상좌표의 상태, 방문여부 확인 후 이동 그리고 visits리스트에 방문좌표 저장
    if nx >= 0 and nx <= m and ny >= 0 and ny <= n:
        if map_list[ny][nx] == 0 and not [nx, ny] in visits:
            visits.append(state[0:2]) 
            state[0] = nx
            state[1] = ny
            count += 1
            cannot_move = 0
            
    # 반복문을 빠져나오기 위한 조건
    if cannot_move ==4:
        break
    cannot_move +=1

print(count + 1)

#################################
# 나동빈 풀이1 #######

n, m = map(int, input().split())

# 방문한 위치를 저장하기위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 형재 캐릭터의 X좌표, Y좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1 , 0 -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0:
        x = nx
        y = ny
    # 뒤가 바다로 막혀있는 경우
    else:
        break
    turn_time = 0

print(count)