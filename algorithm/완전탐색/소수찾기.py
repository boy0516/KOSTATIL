#########################
# 내 풀이

arr=[]

def sosu(num):
    if num:
        num_int = int(num)
    else: return False

    if num_int ==1:
        return False
    else:
        for i in range(2,num_int):
            if num_int%i==0:
                return False
    return True

def find(numbers, num):
    answer = 0
    print(num)
    if sosu(num):
        answer += 1

    for i in range(len(numbers)):
        num2 = num
        if len(num2)==0 and numbers[i]=='0':
            continue
        else:
            num2 += str(numbers[i])
            if not num2 in arr:
                arr.append(num2)
                answer += find(numbers[0:i]+numbers[i+1:],num2)
    return answer

def solution(numbers):
    answer = 0
    num=""
    answer = find(numbers,num)


    return answer

#############################
# 내 풀이 최적화
arr=[]

def sosu(num):  
    if num == 1:
        return 0
    else:
        for i in range(2,num//2+1):
            if num%i==0:
                return 0
    return 1

def find(numbers, num):
    
    for i in range(len(numbers)):
        num2 = num
        if len(num2)==0 and numbers[i]=='0':
            continue
        else:
            num2 += str(numbers[i])
            arr.append(int(num2))
            find(numbers[0:i]+numbers[i+1:],num2)
                   
def solution(numbers):
    answer = 0
    num=""
    find(numbers,num)
    for i in set(arr):
        answer += sosu(i)
    
    return answer