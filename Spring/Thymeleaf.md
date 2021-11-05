# Thymeleaf

 디펜던시 추가

```
		<dependency>
			<groupId>org.thymeleaf</groupId>
			<artifactId>thymeleaf</artifactId>
			<version>2.1.5.RELEASE</version>
		</dependency>
		
		<dependency>
			<groupId>org.thymeleaf</groupId>
			<artifactId>thymeleaf-spring4</artifactId>
			<version>2.1.5.RELEASE</version>
		</dependency>
```



servlet설정

```
<bean id="templateResolver" class="org.thymeleaf.templateresolver.ServletContextTemplateResolver">
		<property name="prefix" value="/view/"></property>
		<property name="suffix" value=".html"></property>
		<property name="templateMode" value="HTML5"></property>
		<property name="characterEncoding" value="UTF-8"></property>
	</bean>
	
	<bean id="templateEngine" class="org.thymeleaf.spring4.SpringTemplateEngine">
		<property name="templateResolver" ref="templateResolver"/>
	</bean>
	
	<bean id="viewResolver4" class="org.thymeleaf.spring4.view.ThymeleafViewResolver">
		<property name="templateEngine" ref="templateEngine"></property>
		<property name="characterEncoding" value="UTF-8"></property>
		<property name="order" value="3"></property>
	</bean>
```





html에 추가

```
<html lang="ko" xmlns:th="http://www.thymeleaf.org">
```

