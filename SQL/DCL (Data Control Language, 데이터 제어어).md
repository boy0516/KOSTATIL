## DCL (Data Control Language, 데이터 제어어)

> DCL은 데이터의 보안, 무결성, 회복, 병행 제어 등을 정의하는 데 사용하는 언어
>
> DCL은 데이터베이스 관리자(DBA)가 데이터 관리를 목적으로 사용한다.

- DCL의 종류

  - COMMIT : 명령에 의해 수행된 결과를 __실제 물리적 디스크로 저장__하고, 데이터베이스 조작 적업이 __정상적으로 완료__되었음을 관리자에게 알려줌

  - ROLLBACK: 데이터베이스 조작 작업이 __비정상적을 종료__되었을 때 __원래의 상태로복구__함

  - GRANT: 데이터베이스 사용자에게 __사용권한__을 __부여__함

  - REVOKE: 데이터베이스 사용자의 __사용권한__을 __취소__함



### GRANT/REVOKE

- 사용자등급

  - DBA: 데이터베이스 관리자

  - RESOURCE: 데이터베이스 및 테이블 생성 가능자

  - CONNECT: 단순 사용자

__이용예시) 사용등급 지정 및 해제__

```
GRANT 사용자등급 TO 사용자_ID_리스트 [IDENTIFIED BY 암호];
REVOKE 사용자등금 FROM 사용자_ID_리스트;

예제) 사용자 ID가 NABI인 사람에게 데이터베이스 및 테이블을 생성할 수 있는 권한을 부여하는 SQL문을 작성하시오.
GRANT RESOURCE TO NABI;

예제) 사용자가 ID가 "STAR"인 사람에게 단순히 데이터베이스에 있는 정보를 검색할 수 있는 권한을 부여하는 SQL문을 작성하시오.

GRANT CONNECT TO STAR;
```



__이용예시) 테이블 및 속성에 대한 권한 부여 및 취소__

```
GRANT 권한_리스트 ON 개체 TO 사용자 [WITH GRANT OPTION];
REVOKE [GRANT OPTION FOR] 권한_리스트 ON 개체 FROM 사용자 [CASCADE];
```

- 권한 종류: ALL, SELECT, INSERT, DELETE, UPDATE, ALTER 등

- WITH GRANT OPTION: __부여받은 권한__을 __다른 사용자에게__ __다시 부여__할 수 있는 권한을 부여함

- GRATN OPTION FOR: 다른 사용자에게 권한을 __부여할 수 있는 권한을 취소__함

- CASCADE: 권한 취소 시 권한을 부여받았던 사용자가 다른 사용자에게 부여한 권한도 __연쇄적으로 취소__함



```
예제) 사용자 ID가 "NABI"인 사람에게 <고객> 테이블에 대한 모든 권한과 다른 사람에게 권한을 부여할 수 있는 권한까지 부여하는 SQL문을 작성하시오.

GRANT ALL ON 고객 TO NABI WITH GRANT OPTION;

예제) 사용자 ID가 STAR인 사람에게 부여한 <고객> 테이블에 대한 권한 중 UPDATE 권한을 다른 사람에게 부여할 수 있는 권한만 취소하는 SQL문을 작성하시오

REVOKE GRANT OPTION FOR UPDATE ON 고객 FROM STAR;

```



### COMMIT

COMMIT은 트랜잭션 처리가 __정상적으로 완료된 후__ 트랜잭션이 수행한 내용을 데이터베이스에 __반영하는 명령__이다. 

COMMIT 명령이 실행하지 않아도 DML문이 성공적으로 완료되면 자동으로 COMMIT되고, DML이 실패하면 자동으로ROLLBACK이 되도록 Auto Commit 기능을 설정할 수 있다.



### ROLLBACK

변경되었으나 아직 COMMIT되지 않은 모든 내용들을 취소하고 데이터베이스를 이전 상태로 되돌리는 명령어이다.

비일관성 상태를 막기 위해 일부만 완료된 트렌젝션은 롤백되어야한다.



### SAVEPOINT

트랜잭션 내에 ROLLBACK 할 위치인 저장점을 지정하는 명령어

저장점 지정할 때는 이름을 부여

ROLLBACK 할 떄 지정된 저장점까지의 트랜잭션 처리 내용이 모드 취소 된다.

```
예제) <사원> 테이블에서 '사원번호'가 40인 사원의 정보를 삭제한 후 COMMIT을 수행하시오

DELETE FROM 사원 WHERE 사원번호 = 40;
COMMIT;

예제) '사원번호'가 30인 사원의 정보를 삭제하시오.
DELETE FROM 사원 WHERE 사원번호 = 30;

예제) SAVEPOINT 'S1'을 설정하고 '사원번호'가 20인 사원의 정보를 삭제하시오

SAVEPOINT S1;
DELETE FROM 사원 WHERE 사원번호 = 20;

예제) SAVEPOINT S1까지 ROLLBACK을 수행
ROLLBACK TO S1;

```



