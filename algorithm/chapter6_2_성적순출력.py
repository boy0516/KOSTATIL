#### 성적이 낮은 순서로 학생 출력하기

# 입력 예시
# 2
# 홍길동 95
# 이순신 77

# 출력 예시
# 이순신 홍길동

#### 내 풀이 #####################
n = int(input())
student = []

for i in range(n):
    student.append(input().split())

def score(data):
    return data[1]

student = sorted(student, key=score)
print(student)
for i in range(n):
    print(student[i][0], end=" ")

#################################
# 나동빈 풀이 ####
# N을 입력받기
n = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

# 키(key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key= lambda student: student[1])  # 람다를 잘 쓰도록 하자

# 정렬이 수행된 결과 출력
for student in array:
    print(student[0], end =" ")