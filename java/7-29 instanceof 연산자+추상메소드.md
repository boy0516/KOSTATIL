복습

- 자식 -> 부모 데이터형으로 자동 변환이 가능하다.
  형변환 이유: 같은 배열에 저장, 하나의 데이터형으로 여러 객체 저장
  기존 자식에게만 있는 변수, 메서드는 호출 불가능

- 오버라이딩 메서드로 구현하면?
     Account에 pay메서드를 만들어주고 CheckingAccount의 pay에서 오버라이딩? 뭔가 이상하다. 매번 이렇게 해주는건 이치에 맞지 않다.

- 다시 본래의 자식 데이터형으로 형 변환(o). 
- 부모에서 자식으로 형변환을 하기위해서는 강제 형변환을 해줘야한다.

```

Account ca = new CheckingAccount("222-2222","홍길동", 10000,"111");
CheckingAccount ca2 = (CheckingAccount)ca;

```

이런식으로 자식에서 부모로 형변환은 자연스럽게 가능하지만

부모에서 자식으로 형변환은 강제 캐스팅을 해야한다.

#### 하지만 잘못된 캐스팅 연산을 주의해야한다.

```
Account ca = new Account("222-2222","홍길동", 10000);
CheckingAccount ca2 = (CheckingAccount)ca;
```

이런 상황에서 원래 부모로 생성된 객체를 자식으로 캐스팅 해줄 수는 없다. 

자식에서 부모로 형변환 해줬을때만 다시 자식으로 형변환 해줄 수 있다.



## instanceof 연산자

형변환 가능한지 검사해주는 연산자

obj instanceof CheckingAccount 이렇게 obj를 CheckingAccount로 캐스트할 수 있을 때만 pay 메소드 호출

반환값으로 boolean값으로 나온다.



# 추상 클래스

추상클래스는 인스턴스화를 검증한다.



추상 메소드의 선언 방법

### `abstract void sendMessage (string recipient);`

- 본체가 없는 메소드를 선언할때 abstract를 앞에 붙여준다

- 메소드의 리턴타입, 이름, 파라미터 변수 선언
- 메소드 본체 대신 세미콜론을 써야함



InputStream => read() => 추상메서드

FileInputStream, DataInputStream, ObjectInputStream

read()					read()						read()

너희들 read()는 가지고 있어야하지 않겠니? 하고 강요하기 위해 만드는데 추상메서드이다.

이것을 상속하게끔해서 반드시 오버라이딩해서 사용하도록 강요하는것



자바에는 서비스객체가 거의 존재한다.

Dao란 data access object

Service객체 ---> Dao객체(OracleDao, MysqlDao)

-> insertSevice()               -> insert() ->oracle insert, insert() -> "mySql insert"



