# collections 모듈 (Counter)

데이터의 개수를 셀 때 유용한 파이썬의 `collections` 모듈의 `Counter` 클래스 사용법을 알아보겠습니다.

## dictionary를 이용한 카운팅

아래 코드는 어떤 단어가 주어졌을 때 단어에 포함된 각 알파멧의 글자 수를 세어주는 간단한 함수입니다.

```py
def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

countLetters('hello world'))
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

이처럼 데이터의 개수를 셀 때 파이썬의 내장 자료구조인 사전(dictionary)이 많이 사용되는데요.

## collections.Counter를 이용한 카운팅

파이썬에서 제공하는 `collections` 모듈의 `Counter` 클래스를 사용하면 위 코드를 단 한 줄로 줄일 수가 있습니다.

```py
from collections import Counter

Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

## collections.Counter 기본 사용법

`collections` 모듈의 `Counter` 클래스는 별도 패키지 설치 없이 파이썬만 설치되어 있다면 다음과 같이 임포트해서 바로 사용할 수 있습니다.

```py
from collections import Counter
```

`collections` 모듈의 `Counter` 클래스는 파이썬의 기본 자료구조인 사전(dictionary)를 확장하고 있기 때문에, 사전에서 제공하는 API를 그대로 다 시용할 수가 있습니다.



- 예시) 주어진 단어에서 가장 많이 등장하는 알페벳과 그 알파벳의 개수를 구하는 함수는 다음과 같이 마치 사전을 이용하듯이 작성할 수 있습니다.

```py
from collections import Counter

def find_max(word):
    counter = Counter(word)
    max_count = -1
    for letter in counter:
        if counter[letter] > max_count:
            max_count = counter[letter]
            max_letter = letter
    return max_letter, max_count

find_max('hello world') # ('l', 3)
```



`Counter` 클래스는 이와 같은 작업을 좀 더 쉽게 할 수 있도록, 데이터의 개수가 많은 순으로 정렬된 배열을 리턴하는 `most_common`이라는 메서드를 제공하고 있습니다.

```py
from collections import Counter

Counter('hello world').most_common() # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
```



```py
from collections import Counter

Counter('hello world').most_common(1) # [('l', 3)]
```



### 출처 : https://www.daleseo.com/python-collections-counter/

### 공식 레퍼런스: https://docs.python.org/3/library/collections.html#collections.Counter
