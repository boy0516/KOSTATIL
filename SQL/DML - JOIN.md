## DML - JOIN

- 연관된 튜플들을 결합하여, 하나의 새로운 릴레이션을 반환한다.
- 일반적으로는 FROM절에 기술하지만, 릴레이션이 사용ㄷ되는 곳 어디에나 사용할 수 있다.
- JOIN은 크게 INNER JOIN과 OUTER JOIN으로 구분된다.



### INNER JOIN

일반적으로 EQUI JOIN과 NON-EQUI JOIN으로 구분된다.

- 조건없는 INNER JOIN을 수행하려면 CROSS JOIN과 동일한 결과를 얻을 수 있다.



#### EQUI JOIN

- EQUI JOIN은 JOIN 대상 테이블에서 공통 속성을 기준으로 '='(equal) 비교에 의해 같은 값을 가지는 행을 연결하여 결과를 생성하는 JOIN방법
- EQUI JOIN은 JOIN 조건이 '='일 때 동일한 속성이 두 번 나타나게 되는데 , 이 중 중복 속성을 제거해 같은 속성을 한번만 보여주는것을 NATURAL JOIN이라고 한다. 
- EQUI JOIN에서 연결 고리가 되는 공통 속성을 JOIN속성이라고 한다.

-------------------

- WHERE절을 이용한 EQUI JOIN의 표기 형식

```
SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
FROM 테이블명1, 테이블명 2, ...
WHERE 테이블명1.속성명 == 테이블명2.속성명;
```

- NATURAL JOIN절을 이용한 EQUI JOIN의 표기 형식

```
SELECT [테이블명1.]속성명, [테이블명2.]속성명, ...
FROM 테이블명1 NATURAL JOIN 테이블명2;
```

- JOIN ~ USING절을 이용한 EQUI JOIN의 표기 형식

```
SELECT [테이블명1.]속성명, [테이블2.]속성명, ...
FROM 테이블명1 JOIN 테이블명2 USING(속성명);
```



#### 예제 테이블 참고 58p

예제) <학생> 테이블과 <학과> 테이블에서 '학과코드' 값이 같은 튜플을 JOIN하여 '학번', '이름','학과코드', '학과명'을 출력하는 SQL문을 작성하시오

```
```

