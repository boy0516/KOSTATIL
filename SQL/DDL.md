## DDL(Data Define Language, 데이터 정의어)

- DB를 구축하거나 수정할 목적으로 사용하는 언어
- 3가지 유형
  - CREATE
    - SCHEMA, DOMAIN, TABLE, VIEW, INDEX __정의__
  - ALTER
    - TABLE에 대한 정의를 __변경__
  - DROP
    - SCHEMA, DOMAIN, TABLE, VIEW, INDEX __삭제__

### CREATE

- 스키마 표기형식

```
CREATE SCHEMA 스키마명 AUTHORIZATION 사용자_id;

#예시)
CREATE SCHEMA 대학교 AUTHORIZATION 홍길동
```

- 도메인 표기형식

``` 
CREATE DOMAIN 도메인명 [AS] 데이터_타입
	[DEFAULT 기본값]
	[CONSTRAINT 제약조건 CHECK (범위값)];
	
#예시)
CREATE DOMAIN SEX CHAR(1) 
	DEFAULT '남' 
	CONSTRAINT VAILD-SEX CHECK(VALUE IN('남', '여'));
```

- 테이블 표기형식

```
CREATE TABLE 테이블명
	(속성명 데이터_타입 [DEFAULT 기본값][NOT NULL],
	[, PRIWARY KEY(기본키_속성명, ...)] 			//기본키 사용 속성
	[, UNIQUE(대체키_속성명, ...)] 				//대체키로 사용할 속성 지정
	[, FOREIGNE KEY(외래키_속성명, ...)]			//외래키 사용 속성 지정
		[REFERENCES 참조테이블(기본키_속성명, ...)] 
		[ON DELETE 옵션]					//참조테이블 삭제시 활동 지정
		[ON UPDATE 옵션]					//참조테이블 속성 변경시 활동 지정
	[, CONSTRAINT 제약조건명][CHECK (조건식)]); //속성값의 제약 조건 정의
	
#예시)
CREATE TABLE 학생 //학생 테이블 생성
	(이름 VARCHAR(15) NOT NULL, 
	학번 CHAR(8),
	전공 CHAR(5),
	성별 SEX,
	생년월일 DATE,
	PRIMARY KEY(학번),//학번을 기본키로 지정
	FOREIGN KEY(전공) REFERENCES 학과(학과코드)) //전공속성을 학과 테이블의 학과코드를 참조하는 외래키로 지정
		ON DELETE SET NULL //학과 테이블에서 튜플이 삭제되면 관련된 모든 튜플의 전공 속성의 값을 NULL로 변경 
		ON UPDATE CASCADE, // 학과 테이블에서 학과코드가 변경되면 관련된 모든 튜플의 전공속성의 값도 같은 값으로 변경한다. 
	CONSTRAINT 생년월일제약
		CHECK(생년월일>='1980-01-01') // 생년월일은 1980-01-01이후만 가능하다.
	);
```



- 뷰 표기형식

```
CREATE VIEW 뷰명[(속성명[, 속성명, ...])]
AS SELECT문;

예제) <고객> 테이블에서 '주소'가 '안산시'인 고객들의 '성명'과 '전화번호'를 '안산고객' 이라는 뷰로 정의하시오

예시)
CREATE VIEW 안산고객(성명, 전화번호)
AS SELECT 성명, 전화번호
FROM 고객
WHERE 주소 = '안산시';
```



- 인덱스 표기형식
  - UNIQUE
    - 사용된경우: 중복값이 없는 속성으로 인덱스 생성
    - 생략된경우: 중복값을 허용하는 속성으로 인덱스를 생성
  - 정렬 여부 지정
    - ASC: 오름차순
    - DESC: 내림차순
    - 생략: 오름차순
  - CLUSTER : 사용하면 인덱스가 클러스터드 인덱스로 설정됨

```
CREATE [UNIQUE] INDEX 인덱스명
ON 테이블명(속성명[ASC|DESC][,속성명 [ASC|DESC]])
[CLUSTER];

예제) <고객> 테이블에서 UNIQUE한 특성을 갖는 '고객번호' 속성에 대해 내림차순으로 정렬하여 '고객번호_idx'라는 이름으로 인덱스를 정의하시오

예시)
CREATE UNIQUE INDEX 고객번호_idx
ON 고객(고객번호 DESC);
```



### ALTER TABLE

- 표기형식

```
ALTER TABLE 테이블명 ADD 속성명 데이터_타입[DEFAULT '기본값']
ALTER TABLE 테이블명 ALTER 속성명 [SET DEFAULT '기본값']
ALTER TABLE 테이블명 DROP COLUMN 속성명 [CASCADE];
```

- - ADD: 새로운 속성(열)을 추가할 때 사용한다.
  - ALTER: 특정 속성의 Default값을 변경할 때 사용한다.
  - DROP COLUMN: 특정 속성을 삭제할 때 사용한다.

```
예제) <학생>테이블에 최대 3문자로 구성되는 '학년' 속성을 추가하시오

예시)
ALTER TABLE 학생 ADD 학년 VARCHAR(3);

##################

예제) <학생> 테이블의 '학번' 필드의 데이터 타입과 크기를 VARCHAR(10)으로 하고 NULL 값이 입력되지 않도록 변경하시오

예시)
ALTER TABLE 학생 ALTER 학번 VARCHAR(10) NOT NULL;
```



### DROP

- 표기형식

```
DROP SCHEMA 스키마명 [CASCADE|RESTRICT];
DROP DOMAIN 도메인명 [CASCADE|RESTRICT];
DROP TABLE 테이블명 [CASCADE|RESTRICT];
DROP VIEW 뷰명 [CASCADE|RESTRICT];
DROP INDEX 인덱스명 [CASCADE|RESTRICT];
DROP CONSTRAINT 제약조건명 [CASCADE|RESTRICT];
```

- - CASCADE: 제거할 요소를 참조하는 다른 모든 객체를 함께 제거한다.
  - RESTRICT: 다른 개체가 제거할 요소를 참조중일 때는 제거를 취소한다.

```
예제) <학생> 테이블을 제거하되, <학생> 테이블을 참조하는 모든 데이터를 함께 제거하시오

예시) DROP TABLE 학생 CASCADE;
```

