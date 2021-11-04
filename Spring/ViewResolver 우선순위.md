# ViewResolver 우선순위

```
<bean id="viewResolver" class="org.springframework.web.servlet.view.InternalResourceViewResolver">
		<property name="prefix" value="/view/"/>
		<property name="suffix" value=".jsp"/>
		<property name="order" value="1"></property>
	</bean>
```

```
<bean id="viewResolver2" class="org.springframework.web.servlet.view.UrlBasedViewResolver">
		<property name="viewClass" value="org.springframework.web.servlet.view.tiles3.TileView"></property>
		<property name="order" value="1"></property>
	</bean>
```

두개의 viewResolver가 있으면

내부에` <property name="order" value="1"></property>`

이렇게 작성해줘서 우선순위를 정해줄 수있다.