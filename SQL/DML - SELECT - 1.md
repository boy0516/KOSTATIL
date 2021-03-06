## DML - SELECT - 1

일반형식

```
SELECT [PREDICATE][테이블명.]속성명 [AS 별칭][,[테이블명.]속성명, ...]
[, 그룹함수(속성명)[AS 별칭]]
[, Window함수 OVER (PARTITION BY 속성명1,속성명2, ...
				ORDER BY 속성명3, 속성명4, ...)]
FROM 테이블명[, 테이블명, ...]
[WHERE 조건]
[GROUP BY 속성명, 속성명, ...]
[HAVING 조건]
[ORDER BY 속성명 [ASC | DESC]];
```

- SELECT절
  - PRECIDATE : 검색할 튜플 수를 제한하는 명령어를 기술함
    - DISTINCT : 중복된 튜플이 있으면 그 중 첫 번째 한 개만 표시함
  - 속성명: 검색하여 부로올 속성(열) 또는 속성을 이용한 수식을 지정함
  - AS: 속성이나 연산의 이름을 다른 이름으로 표시하기 위해 사용함
- FROM절: 검색할 데이터가 들어있는 테이블의 이름을 기술함
- WHERE절 : 검색할 조건을 기술함
- ORDER BY절: 데이터를 정렬하여 검색할 때 사용함
  - 속성명: 정렬의 기준이 되는 속성명을 기술함
  - [ASC | DESC] : 정렬 방식으로 ASC는 오름차순, DESC는 내림차순이다. 생략하면 오름차순으로 정리



조건 연산자

- LIKE 연산자: 대표 문자를 이용해 지정된 속성의 값이 문자 패턴과 일치하는 튜플을 검색하기 위해 사용된다.

  - `%` : 모든 문자를 대표함
  - `_` : 문자 하나를 대표함
  - `#` : 숫자 하나를 대표함 

  

__예제 테이블은 31p 참고__

예제) <사원> 테이블의 모든 퓨틀을 검색하시오

```
SELECT * FROM 사원;
SELECT 사원.* FROM 사원;
SELECT 이름, 부서, 생일, 주소, 기본급 FROM 사원;
SELECT 사원.이름, 사원.부서, 사원.생일, 사원.주소, 사원.기본급 FROM 사원;
```



예제) <사원>테이블에서 '주소'만 검색하되 같은 '주소'는 한 버난 출력하시오.

```
SELECT DISTINCT 주소 FROM 사원;
```



예제) <사원> 테이블에서 '기본급'에 특별수당 10을 더한 월급을 "XX부서의 XXX의 월급 XXX" 형태로 출력하시오.

```
SELECT 부서 + '부서의' AS 부서2, 
이름 + '의 월급' AS 이름2, 
기본급 + 10 AS 기본급2 
FROM 사원;
```



예제)<사원> 테이블에서 '기획'부의 모든 튜플을 검색하시오.

```
SELECT * FROM 기획 WHRER 부서 = '기획';
```

 

예제) <사원> 테이블에서 '기획' 부서에서 근무하면서 '대흥동'에 사는 사람의 튜플을 검색하시오

```
SELECT * FROM 사원 WHERE 부서 = '기획' AND 주소 = '대흥동';
```



예제)<사원> 테이블에서 '부서'가 '기획'이거나 '인터넷'인 튜플을 검색하시오.

```
SELECT * FROM 사원 WHERE 부서 = '기획' OR 부서 = '인터넷';
```



예제)<사원> 테이블에서 성이 '김'인 사람의 튜플을 검색하시오.

```
SELECT * FROM 사원 WHERE 이름 LIKE "김%";
```



예제)<사원> 테이블에서 '생일'이 '01/01/69'에서 '12/31/73' 사이인 튜플을 검색하시오.

```
SELECT * FROM 사원 WHERE 생일 BETWEEN #01/01/69# AND #12/31/73#;
```



예제)<사원> 테이블에서 '주소'가 NULL인 튜플을 검색하시오.

```
SELECT * FROM 사원 WHERE 주소 IS NULL;
```

 

예제)<사원>테이블에서 '주소'를 기준으로 내림차순 정렬시켜 상위 2개 튜플만 검색하시오.

```
SELECT TOP 2 * FROM 사원 ORDER BY 주소 DESC;
```



예제)<사원> 테이블에서 '부서'를 기준으로 오름차순 정렬하고, 같은 '부서'에 대해서는 '이름'을 기준으로 내림차순 정렬시켜서 검색하시오.

```
SELECT * FROM 사원 ORDER BY 부서 ASC, 이름 DESC;
```



#### 하위 질의

하위 질의는 조건절에 주어진 질의를 먼저 수행하여 그 검색 결과를 조건절의 피연산자로 사용한다.



예제) '취미'가 ''나이트댄스''인 사원의 '이름'과 '주소'를 검색하시오

```
SELECT 이름, 주소 
FROM 사원 
WHERE 이름 = (SELECT 이름 FROM 여가활동 WHERE 취미 = '나이트댄스');
```



예제) 취미활동을 하지 않는 사람들을 검색하시오

- 없는거 찾을때는 NOT IN

```
SELECT *
FROM 사원
WHERE 이름 NOT IN (SELECT 이름 FROM 여가활동);
```



예제) 취미활동을 하는 사람들의 부서를 검색하시오.

- 있는거 찾을때는 EXISTS

```
SELECT 부서
FROM 사원
WHERE 이름 EXISTS (SELECT 이름 FROM 여가활동.이름 = 사원.이름);
```



예제) 경력이 10년 이상인 사원의 이름, 부서, 취미, 경력을 검색하시오

```
SELECT 사원.이름, 사원.부서, 여가활동.취미, 여과활동.경력
FROM 사원, 여거활동
WHERE 여가활동.경력 >= 10 AND 사원.이름 = 여가활동.이름;
```

