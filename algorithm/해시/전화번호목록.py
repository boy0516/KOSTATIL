def solution(phone_book):
    answer = True
    hash_table = {} #파이썬에는 딕셔너리가 있으니까 딕셔너리를 해시테이블로 사용
    phone_len = [] #겹칠 수 있는 길이를 저장

    #각 번호들의 길이를 phone_len 리스트에 저장
    for phone in phone_book: 
        phone_len.append(len(phone))

    # 중복되는 길이 제거
    phone_len = set(phone_len) 

    # 해시테이블에 넣는작업 hashing은 굳이 안함
    for i in phone_book:
        hash_table[i] = True

    # 겹치는 번호가 있는지 체크
    for i in phone_len: 
        for phone in phone_book:
            if len(phone) > i:
                try:
                    if hash_table[phone[0:i]]:
                        return False
                except:
                    continue

    return answer