# tiles(template기술)

- 페이지 모듈화 (header, body, footer)

순서

1. pom.xml에서 tiles-jsp, tiles-servlet, 

```
<!-- https://mvnrepository.com/artifact/org.apache.tiles/tiles-jsp -->
		<dependency>
			<groupId>org.apache.tiles</groupId>
			<artifactId>tiles-jsp</artifactId>
			<version>3.0.7</version>
		</dependency>
		<!-- https://mvnrepository.com/artifact/org.apache.tiles/tiles-servlet -->
		<dependency>
			<groupId>org.apache.tiles</groupId>
			<artifactId>tiles-servlet</artifactId>
			<version>3.0.7</version>
		</dependency>
		<!-- https://mvnrepository.com/artifact/org.apache.tiles/tiles-core -->
		<dependency>
			<groupId>org.apache.tiles</groupId>
			<artifactId>tiles-core</artifactId>
			<version>3.0.7</version>
		</dependency>
```



2. tiles2def.xml, template파일 설정

커스텀 태그 적용

```
<%@ taglib prefix="tiles" uri="http://tiles.apache.org/tags-tiles" %>    
```

3. servlet.xml => tiles관련 설정

```
<!-- Tiles Setting -->
	<bean id="tilesConfigurer" class="org.springframework.web.servlet.view.tiles3.TilesConfigurer">
		<property name="definitions">
			<list>
				<value>/WEB-INF/tiles2def.xml</value>
			</list>
		</property>
	</bean>
```



4. 지금까지는 ViewResolver가 jsp용이었는데 이걸 tiles용으로 바꿔줘야한다.

```
<bean id="viewResolver2" class="org.springframework.web.servlet.view.UrlBasedViewResolver">
		<property name="viewClass" value="org.springframework.web.servlet.view.tiles3.TilesView"></property>
	</bean>
```



5. tiles2def.xml

```
<tiles-definitions>
	<definition name="base_layout" template="/view/module/template.jsp">
		<put-attribute name="header" value="/view/module/header.jsp"/>
		<put-attribute name="footer" value="/view/module/footer.jsp"/>
		<put-attribute name="logo" value="/view/module/logo.jsp"/>
	</definition>
	
	<definition name="insert_form" extends="base_layout">
		<put-attribute name="body" value="/view/insert_form.jsp"/>
	</definition>
	
	<definition name="list" extends="base_layout">
		<put-attribute name="body" value="/view/list.jsp"/>
	</definition>
	
</tiles-definitions>
```

이때 definition 네임이랑 jsp 이름이랑 맞춰줘야 인식됨



템플릿에 표시해줘야함

```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="tiles" uri="http://tiles.apache.org/tags-tiles" %>    
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
	<!-- 헤더영역 -->
	<tiles:insertAttribute name="header"/>
	<hr>
	<tiles:insertAttribute name="logo"/>
	<hr>
	<!-- 바디영역 -->
	<tiles:insertAttribute name="body"/>
	<hr>
	
	<!-- 푸터영역 -->
	<tiles:insertAttribute name="footer"/>
</body>
</html>
```

