# Spring&Mybatis 연결

- pom.xml에 spring-jdbc, mybatis, mybatis-spring 을 받는다.

- WEB-INF 폴더에 mybatis-config.xml을 생성한다.
- mapper패키지에 board.xml을 생성한다.
- 

1. server.xml => ><resource name="jdbc/oracle" type="DataSource"

2. dataSource =>

   JNDI는 디렉터리 서비스에서 제공하는 데이터 및 객체를 발견하고 참고하기 위한 자바 API다. JNDI는 일반적으로 다음의 용도로 쓰인다: 자바 애플리케이션을 외부 디렉터리 서비스에 연결 자바 애플릿이 호스팅 웹 컨테이너가 제공하는 구성 정보를 참고.

3. sqlSessionFactory 생성 <-- dataSource, mybatis-config.xml위치

4. sqlSessionTemplate생성 <--sqlSessionFactory

5. BoardDao <== sqlSessionTemplate

6. BoardController <== BoardDao



176page

hicariconfig, dataSource, sqlSessionFactory, mybatis-spring



BoardMapper인터페이스, Board.xml ==>4qjs



201page

class BoardDao

​	@AutoWired

​	private BoardMapper mapper;

​	public void insert(Board board){

​		mapper.insert(board);

​	}



202 page

<context:component-scan base-package="kosta.model">





## DB관련

1. Board.xml  ==> select추가
2. BoardMapper.java ==> 메서드 추가
3. BoardDao 메서드 추가
4. BoardController Dao메서드 호출



