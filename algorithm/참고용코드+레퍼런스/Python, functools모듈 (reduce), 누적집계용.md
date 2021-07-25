# functools모듈 (reduce) 

파이썬의 `functools` 내장 모듈의 `reduce()` 함수는 여러 개의 데이터를 대상으로 주로 누적 집계를 내기 위해서 사용합니다.

기본적으로 초기값을 기준으로 데이터를 루프 돌면서 집계 함수를 계속해서 적용하면서 데이터를 누적하는 방식으로 작동합니다.

```py
reduce(집계 함수, 순회 가능한 데이터[, 초기값])
```

여기서, 집계 함수는 두개의 인자를 받아야 하는데요. 

첫번째 인자는 누적자(accumulator), 

두번째 인자는 현재값(current value)가 넘어오게 됩니다. 

누적자는 함수 실행의 시작부터 끝까지 계속해서 재사용되는 값이고, 현재값은 루프 돌면서 계속해서 바뀌는 값입니다.



## 실습 데이터 생성

파이썬 인터프리터에서 다음과 같이 유저 5명의 데이터를 임의로 생성합니다. 5개의 dictionary를 담고 있는 list 입니다.

```py
>>> users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M', 'age': 73},
... {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F', 'age': 29},
... {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M', 'age': 51},
... {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F', 'age': 32},
... {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F', 'age': 42}]
```



## 임포트

`reduce()`는 내장 함수가 아니기 때문에 `functools` 내장 모듈을 통해서 임포트를 해줘야 사용할 수 있습니다.

```py
>>> from functools import reduce
```



## 나이 합계 구하기

그럼, 실습 데이터를 대상으로 `reduce()` 함수를 사용해서 유저들의 나이의 합을 구해보도록 하겠습니다.

```py
>>> reduce(lambda acc, cur: acc + cur["age"], users, 0)
227
```



누작자에 초기값 `0`이 세팅되고, 그 다음 각 유저의 나이가 집계 함수에 의해서 계속해서 더해지게 됩니다.

다음과 같이 `reduce()` 함수의 실행 과정을 직접 따라가보면 좀 더 이해가 쉬우실 것입니다.

```py
>>> 0
0
>>> 0 + 73
73
>>> 73 + 29
102
>>> 102 + 51
153
>>> 153 + 32
185
>>> 185 + 42
227
```



## 성별로 분류 하기

`reduce()` 함수는 데이터 그룹핑(data grouping)과 같이 좀 더 복잡한 누적 집계에도 활용될 수 있습니다.

예를 들어, 유저 이름을 성별에 따라 분류해보도록 하겠습니다. 람다 함수를 사용하기에는 다소 복잡한 케이스이므로, `names_by_sex()`라는 함수를 하나 선언하도록 하겠습니다.

```py
>>> def names_by_sex(acc, cur):
...     sex = cur["sex"]
...     if sex not in acc:
...         acc[sex] = []
...     acc[sex].append(cur["name"])
...     return acc
...
```

`reduce()` 함수에 `names_by_sex` 함수를 인자로 넘기면, 성별을 키로 이름 list를 값으로 갖는 dictionary를 얻게 됩니다.

```py
>>> reduce(names_by_sex, users, {})
{'M': ['Brett Holland', 'Michael Jenkins'], 'F': ['Madison Martinez', 'Karen Rodriguez', 'Amber Rhodes']}
```



## 초기값의 중요성

`reduce()` 함수를 사용할 때 많은 분들이 실수하는 부분이 있는데 바로 초기값 세팅 유무에 따라 이상한 결과가 나올 수 있는 것입니다.

예를 들어, 유저의 나이 합계를 구하는 예제에서 초기값으로 `0`을 넘겨주지 않으면 `TypeError`가 발생합니다.

```py
>>> reduce(lambda acc, cur: acc + cur["age"], users)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    reduce(lambda acc, cur: acc + cur["age"], users)
  File "<input>", line 1, in <lambda>
    reduce(lambda acc, cur: acc + cur["age"], users)
TypeError: unsupported operand type(s) for +: 'dict' and 'int'
```



다른 예로, 유저 이름을 성별에 따라 분류하는 예제에서 초기값으로 빈 dictionary을 넘겨주지 않으면 다음과 같이 예상치못한 결과가 나옵니다.

생략..

이런 현상이 발생하는 이유는 `reduce()` 함수에 초기값을 넘기지 않으면 두번째 인자로 넘어온 list나 tuple의 첫번째 값이 초기값으로 사용되기 때문입니다. 본 예제에서 사용하고 있는 실습 데이터는 첫번째 값이 유저 정보를 담고 있는 dictionary이므로 이 값에 숫자를 더하거나, 키를 추가하려고 하니 문제가 발생하는 것입니다.



## 마치면서

이상으로 여러 개의 데이터를 대상으로 주로 누적 집계를 내기 위해서 사용하는 파이썬의 `functools` 내장 모듈의 `reduce()` 함수에 대해서 알아보았습니다. `reduce()`는 파이썬의 내장 함수인 `map()`, `filter()`와 함께 함수형 프로그래밍에서는 매우 자주 사용되는 개념이니 잘 이해하시고 활용하셨으면 좋겠습니다.



## 출처 : https://www.daleseo.com/python-functools-reduce/

