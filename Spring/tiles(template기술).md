# tiles(template기술)

- 페이지 모듈화 (header, body, footer)

순서

1. pom.xml에서 tiles-jsp, tiles-servlet, 

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
		<property name="viewClass" value="org.springframework.web.servlet.view.tiles3.TileView"></property>
	</bean>
```



