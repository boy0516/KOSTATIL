##############################
# 내풀이 #####################
# 주먹구구식 풀이의 끝판왕

def solution(genres, plays):
    answer = []
    # 무려 세개의 테이블 ㅋㅋ
    genre_table = {}
    reverse_table = {}
    table = {}

    # 장르별 재생 횟수를 담은 딕셔너리생성
    # key는 장르명, values는 재생횟수
    for i in range(len(genres)):
        try: 
            table[genres[i]].append([i, plays[i]])
        except:
            table[genres[i]] = [[i, plays[i]]]


    # 각 장르별 앨범들 고유번호와 재생횟수를 담은 딕셔너리 생성
    # key는 장르명, values는 [[고유번호, 재생횟수]] 2차원배열
    for i in range(len(genres)):
        try: 
            if genre_table[genres[i]]:
                genre_table[genres[i]] += plays[i]
        except:
            genre_table[genres[i]] = plays[i]


    # 재생횟수가 겹치지 않으니까 키 밸류를 바꿔버린 딕셔너리 생성
    for i in genre_table:
        reverse_table[genre_table[i]] = i


    # 키 값들을 내림차순 정렬하고 하나씩 가져다 쓰기
    for i in sorted(reverse_table, reverse=True):
        count = 0
        # table에 담긴 앨범정보 가져와서 재생횟수로 내림차순
        for j in sorted(table[reverse_table[i]], key = lambda x: x[1], reverse=True):
            answer.append(j[0])
            count += 1
            # 두번 가져오면 탈출
            if count ==2:
                break

    return answer

##########################
# 다른 사람 풀이 ########

def solution(genres, plays):
    answer = []
    
    # set으로 중복 제거하면서 딕셔너리의 키값으로 넣어줌
    d = {e:[] for e in set(genres)}

    # zip을 사용해서 genres와 plays, 고유번호 인덱스를 동시에 묶어서 처리해줌
    # 이런 편리한 방법이..
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])

    # 딕셔너리의 키값을 가져오고 lambda식을 이용해서 d[키값]으로 values값을 가져온다.
    # y에 [plays, 고유번호] 를 전달하고 plays의 수로 정렬해줌
    # genreSort에는 재생횟수로 정렬된 키값이 리스트로 전달
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)

    # 키 순서대로 반환
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer