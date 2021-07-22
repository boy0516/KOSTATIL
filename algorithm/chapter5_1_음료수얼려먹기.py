#### 음료수 얼려 먹기

# 입력예시 150p 참고
# 출력예시

#### 내 풀이 #####################

####################실패.....########


#################################
# 나동빈 풀이 ########
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] =1
        dfs(x - 1 ,y)
        dfs(x, y - 1)
        dfs(x + 1 , y)
        dfs(x, y + 1)
        return True

    return False

result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출려