# log4jdbc

저번에 했던 DB설정에서 다음을 변경해준다. 

```
<bean id="hikariConfig" class="com.zaxxer.hikari.HikariConfig">
		<property name="driverClassName" value="net.sf.log4jdbc.sql.jdbcapi.DriverSpy"/> //여기 패키지 가져온는거랑
		<property name="jdbcUrl" value="jdbc:log4jdbc:oracle:thin:@localhost:1521:XE"></property> //여기를 변경
		<property name="username" value="kosta223"/>
		<property name="password" value="1234"/>
	</bean>
```



- driverClassName

- jdbcUrl

이 두가지를 변경



이거 변경해주면 다음과 같이 편리한 로그가 함께 출력된다.

![image-20211108100157417](assets\image-20211108100157417.png)

 이런 느낌

이용한 쿼리문이랑 결과에 대해서 나와서 편리한다.

