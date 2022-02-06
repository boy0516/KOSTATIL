kafka 하고 rabbitmq에 대해서 찾아보는걸 권장한다.

프로젝트를 함에 있어서 뭐가 적당한지 비교를 해보시길 바랍니다.

찾아보시길 권합니다.

테스트를 하다가 만 상태이기 때문에 마이크로서비스 하기전에 카푸카 하고 넘어가겠습니다.

앞에 보시면 주키퍼 서버를 가동하고있습니다.
카푸카도 돌리고있고
메시지를 만드는건 프로듀서
메시지를 쓰는건 컨슈머

파티션에 분산되어 저장되는데 
카푸카를 여러개 만들어서 기동해야 파티션을 나누는게 의미가 있는거지 싱글노드에는 별로 의미가 없다.

파티션이라는 개념에 설치를 한다. 

특징을 한번 클라우드 네이티브 아키텍처 4가지를 보면 
1. msa
2. 컨테이너 가상화 
3. CICD자동화
4. Devops

원래 이번주 배우는것은 msa이죠.
강조했지만 모노리스가 나쁜것은 아니죠. 개발속도가 빠를 수 있죠. 마이크로소프트 아키텍처는 개별적인 서비스를 나눠서 만드는것이다. 

마이크로 서비스라는것이 만들어져있는 서비스가 등록되어져있는지 
마이크로 서비스가 만들어졌을떄 정보를 저장하고 어떤 정보를 가지고있는지 ??

서비스 매쉬에서 필요한 마이크로서비스를 서비스 디스커버리에 등록한다.

서비스 디스커버리 중요하다. 기억하자

또 서비스 매쉬에 로드밸런서가 있다.

시스템단에서 처리하는 방식과 어플리케이션 안에서 처리하는 방식이있는데 
시스템단에서 처리하는방식이 훨씬 좋은 방식이다.

진입점에서 클라이언트 요청이 들어오면 어디로 갈지 판단을 해야하는데 서비스 디스커버리에서 판단을하지

리드 명령을 받았을때는 그냥 가지고있는 정보 주면된다. 

update요청을 받으면 자기가 처리한 다음에 다른사람에게 알려줘야한다. ㅇ=

msa->API 사용

Resourse에 다이렉트로접속하는것을 막는다. 

이벤트 스트림. 

정보가 들어오면 토픽에 등록하고 관심있다고 등록하는 컨슈머들은 데이터들을 가져가서 반영한다. 

서비스 디스커버리에다가. 정보를 물어보죠 어디로 갈지 로드벨런서가 방향을 정해주고. 이런거를 다 해주는 구성요소가 서비스 메쉬이다. 서비스 메쉬는 하나의 개념이다. 부하분산 공유데이터를 보관하고있다.

a가 3개정도서버에 배포되어있는데
db를 별도로 분리시켜 만들면 편하다.

a에서 db로 직접 컨트롤하면 편하지만 바람직하지 않다.

배포를 다시 하지 않기위해서 a는 메시지 큐잉 서비스를 상대할것이다.

변화가 있으면 메시지큐잉서비스에 update를 보내주면 메시지큐잉서비스가 db를 상대한다.

Replica 세팅이라고 해서 insert, update, delete가 감지되면 복제본 db2에 저장을 해준다. 


msa방식의 단점중 하나는
단점중에 하나는 네트워크 트레픽 비용이 많이 든다.
네트워크 트레픽이 많이 생긴다는 이야기는 클라우드를 쓰면 돈이 많이 든다는것이다. 



CQRS라는 용어를 기억해둬라.



카프카에서 저장되는것이 토픽이고 파티션으로 분산되어 저장될 수 있다. 


카푸카에서 다양한 언어 지원 서드파티 라이브러리 지원

---------------
카푸카를 db와 연결하기 위해서 드라이버가 필요하다

https://mvnrepository.com/artifact/org.mariadb.jdbc/mariadb-java-client/2.7.2

여기서 jar 파일 다운

이제 db를 만들어보자 
create database mydb;
use mydb;

create table users(
	id int auto_increment primary key,
	user_id varchar(20) not null,
	pwd varchar(20) not null,
	created_at datetime default now()
)


카푸카 커넥터 다운로드
curl -O http://packages.confluent.io/archive/6.1/confluent-community-6.1.0.tar.gz


Kafka Connect 실행
- ./bin/connect-distributed ./etc/kafka/connect-distributed.properties

그러면 이런게 뜬다
Classpath is empty. Please build the project first e.g. by running 'gradlew jarAll'

그러면 
.\bin\windows\kafka-run-class.bat를 찾아서 

다음 문장을 
- rem Classpath addition for core 위에 추가해준다.

rem classpath addition for LSB style path
if exist %BASE_DIR%\share\java\kafka\* (
	call:concat %BASE_DIR%\share\java\kafka\*
)

그러고나면 실행이 되는데 
java.io.FileNotFoundException: C:\Users\choi\Work\confluent-6.1.0\config\tools-log4j.properties (지정된 경로를 찾을 수 없습니다)

이런 에러가 하나 날 수 있는데 이건 로그를 생성하기위한 설정파일이 없어서 나는것으로 신경쓰이면 경로로 가서 만들어주면된다. 
C:\Users\choi\Work\confluent-6.1.0\config

파일이름은 이렇게
tools-log4j.properties

내용은 이렇게 
log4j.rootLogger=ERROR

실행되었으면 기본으로 생성되는 토픽을 확인해본다

$ bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
__consumer_offsets
connect-configs
connect-offsets
connect-status

api로 불러올수 있는지 확인

$curl http://localhost:8083/connectors
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100     2  100     2    0     0    125      0 --:--:-- --:--:-- --:--:--   125
[]


jDBC 자바 데이터페이스 커넥터 설정이다

자바에서 데이터베이스 연결할때 쓰는 api통틀어서 jdbc라고 한다.

kafka자체가 자바기반으로 만들어져있기 때문에 다양한 드라이버 형태가 만들어지는데 jdbc형태로 만들어야한다. 

https://docs.confluent.io/5.5.1/connect/kafka-connect-jdbc/index.html 로 이동해서 zip파일 다운로드 받는 링크로 이동해서 다운로드 해준다.

이것을 압축해제한 경로를 C:\Users\choi\Work\confluentinc-kafka-connect-jdbc-10.1.0\lib

C:\Users\choi\Work\confluent-6.1.0\etc\kafka\connect-distributed.properties 의 

맨 마지막의 
plugin.path를
plugin.path=\C:\\Users\\choi\\Work\\confluentinc-kafka-connect-jdbc-10.1.0\\lib

이렇게 해준다. 

주의해줘야할게 중간에 \를 두개씩 써줘야한다. 역슬래쉬 두개 !!

자 이렇게 넣어주면 이제 토픽을 생성해줘야겠죠? 그러려면 소스커넥트를 해줘야합니다

Kafka Source Connect 추가

echo '
{
"name" : "my-source-connect",
"config" : {
"connector.class" : "io.confluent.connect.jdbc.JdbcSourceConnector",
"connection.url":"jdbc:mysql://localhost:3306/mydb",
"connection.user":"root",
"connection.password":"test1357",
"mode": "incrementing",
"incrementing.column.name" : "id",
"table.whitelist":"users",
"topic.prefix" : "my_topic_",
"tasks.max" : "1"
}
}
' | curl -X POST -d @- http://localhost:8083/connectors --header "content-Type:application/json"

이렇게 전체를 명령어로 치던가 

좀더 쉽게 하려면 postman을 이용하면

http://localhost:8083/connectors 에서 post명령어로 

헤더에 content-Type을 application/json으로 해주고 

바디에다가 
{
"name" : "my-source-connect",
"config" : {
"connector.class" : "io.confluent.connect.jdbc.JdbcSourceConnector",
"connection.url":"jdbc:mysql://localhost:3306/mydb",
"connection.user":"root",
"connection.password":"test1357",
"mode": "incrementing",
"incrementing.column.name" : "id",
"table.whitelist":"users",
"topic.prefix" : "my_topic_",
"tasks.max" : "1"
}
}
를 입력해주고 보내면 소스 커넥트가 생성이 된다.

201ok로 반응 오는것을 확인하기 

그러고 나서 source connect 확인하면 (GET)
http://localhost:8083/connectors를 GET방식으로 해주면 추가된것을 확인할 수 있다.

그러고 토픽 리스트를확인하는데 이때 db가 비어있으면 토픽이 안보이니까 
db에 데이터를 넣어주면 토픽이 보인다.



이렇게 잘 가지고 놀았으면 끊어줄 수도 있어야하는데 
커넥트를 제거하는명령어는 다음과 같다.

HTTP DELETE method로 http://localhost:8083/connectors/[생성한 source connect의 이름]

현상황 리뷰
주키퍼가 기동되어있는 상태+카프카가 기동되어있는 상태이다.

거기에 커넥트를 연결했다. 

소스커넥터를 추가하면서 거기의 정보를 어떻게 저장했는지 기억하나요? 데이터베이스에 접속하기위한 커넥션 url이 있을겁니다. 그리고 아아피 페스워드 , 데이터베이스 이름.

거기에 화이트리스트에 테이블 이름이 있습니다.

인서트 작업을 했어요. 쿼리를. 우리는 프로그래밍 언어를 통해서도 쿼리를 쏠 수 있죠. 그러면 users라는 테이블이 변경이 되죠. 

변경된 데이터를 어디에 저장하냐면 topic.prefix라는 것이 있죠. my_topic_이렇게 있고 

그러면 my_topic_users라는 토픽이 생성이 되고 거기에 저장이 된다. 

insert를 하면 감지를하고 토픽에 데이터가 전달이 된다. 

콘솔 프로듀서
파이썬 프로듀서 파이

어떤 프로듀서가 되었던간에 데이터를 추가하면 토픽에 데이터가 들어간다.

우리 생각대로 마지막 토픽에 저장이 되어야할거같아요.

그런데 문제는 db가 문제에요. 

db는 토픽에서 db로 가져오는것을 설정을 안해놨다는겁니다. 

백날 토픽에 올려도 db 에는 안올려지는데 

이런걸 해주기 위해서 sink라는 것을 해줘야한다. 

한마디로 

db --->토픽으로는 소스connect

토픽 --->db는 sink 이다.

--------
오늘 문제가 어마어마하네 1시간 이상 걸림.
-----------
kafka topic이 있고 
토픽에 데이터를 밀어 넣는 일을 해왔죠. 
소스 커넥터가 db를 읽고 밀어 넣어줬죠. 

데이터들을 가져다가 우리가 다른 리소스 다른 타겟에 넣고싶은데 이때 sink 커넥터가 해줬어요.

그런데 문제는 싱크 커넥터가 topic에서 가져왔어요. 

이걸 읽어왔을떄 db에 어떤 형태로 들어가야할지 sink커넥터는 몰라요. 

우리가 넣어야할 db는 정형화된 데이터에요. 컬럼이 정해져있죠.

이런 json포맷을 어떻게 저장해줄지는 

json의 정보를 보고 넣어줘야하는데 

안되는게 뭐냐

어제 만들었던 포맷과 맞지 않는 데이터떄문에 안되었다. 

스키마가 들어가있어야하고
페이로드가 들어가있어야한다. 

스키마는 어떤 테이블에 어떤 컬럼에 어떤 사이즈인지
페이로드는 이 스키마에 맞는 정보를 가지고있다.

그래서 이 둘이 한 세트가 되어서 들어간다. 

http://localhost:8083/connectors

{
	"name" : "my-sink-connect",
	"config" : {
		"connector.class" : "io.confluent.connect.jdbc.JdbcSinkConnector",
		"connection.url":"jdbc:mysql://localhost:3306/mydb",
		"connection.user":"root",
		"connection.password":"mysql",
		"auto.create":"true",
		"auto.evolve":"true",
		"delete.enabled":"false",
		"tasks.max":"1",
		"topics":"my_topic_users"
	}
}