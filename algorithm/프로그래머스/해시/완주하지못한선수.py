def solution(participant, completion):

    hash_table = {} # 파이썬엔 딕셔너리가 있으니까 이걸 해시테이블로 사용

    for i in participant: # 참가자들을 테이블에 넣기
        try:
            if hash_table[i]: # 테이블에 있으면 동명이인 1씩 추가
                hash_table[i] +=1
        except:
            hash_table[i] = 1 #테이블에 존재하지 않으면 추가
            
    for j in completion: #완주자들 확인하고 1씩 빼주기
        hash_table[j] -= 1
    
    for k in participant: #테이블에 남아있는 이름 확인 후 반환
        if hash_table[k] == 1:
            return k