def solution(m, n, puddles):
    answer = 0
    arr = [[0]*(m) for _ in range(n)]
    puddle_dict={}

    arr[1][0]=1
    arr[0][1]=1

    for puddle in puddles:
        if puddle==[1,2]:
            arr[1][0]=0
        if puddle==[2,1]:
            arr[0][1]=0
        puddle_dict[(puddle[0]-1,puddle[1]-1)]=1

    if arr[1][0]==0 and arr[0][1]==0:
        return 0

    for y in range(n):
        for x in range(m):
            try:
                puddle_dict[(x,y)]

            except:    
                if x==0 and y==0:
                    continue
                elif y==0:
                    arr[y][x] += arr[y][x-1]
                elif x==0:
                    arr[y][x] += arr[y-1][x]
                else:
                    arr[y][x] += (arr[y][x-1]+arr[y-1][x])

    answer = arr[n-1][m-1]

    return answer%1000000007