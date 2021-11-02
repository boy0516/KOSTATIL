Spring Eureka

service Discovery

서비스가 어떤 위치에 있는지 key value형식으로 등록해서 

검색할 수 있도록하는 서비스에 등록할것이다.

클라이언트 

로드밸런스 - API gateway - serviceDiscovery

EcommerceDiscoveryService

사용자 서비스, 상품서비스

E-commerce

## VM option에서

```
-Dserver.port=9002
```

이렇게 실행 옵션을 지정해줄수 있다.



cmd로 실행하는 방법1

```
mvnw spring-boot:run -Dspring-boot.run.jvmArguments='-Dserver.port=9003'
```



cmd로 실행하는 방법2

```
compile 선행

java -jar -Dserver.port=9004 .\target\user-service-0.0.1-SNAPSHOT.jar
```



