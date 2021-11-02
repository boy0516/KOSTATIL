# Spring MVC

오늘은 기본적이 구조파악을 위해서 다이나믹 웹 프로젝트를 maven프로젝트로 변환해서 수업을 진행

1. pom.xml 수정

```
  <dependencies>
	<dependency>
		<groupId>org.springframework</groupId>
		<artifactId>spring-webmvc</artifactId>
		<version>4.3.2.RELEASE</version>
	</dependency>
  </dependencies>
```

디펜던시를 추가해준다.



2. springapp-service.xml

   webcontent의 web-inf 안에 스프링 빈 컨피그파일을 만들고 다음과 같이 빈들을 넣어준다.

   컨트롤러와 view를 연결해주는 viewResolver를 빈으로 넣어준다.

```
<bean id="helloController" class="kosta.controller.HelloController"></bean>
	<bean id="boardController" class="kosta.controller.BoardController"></bean>
	
	<bean id="viewResolver" class="org.springframework.web.servlet.view.InternalResourceViewResolver">
		<property name="prefix" value="/view/"/>
		<property name="suffix" value=".jsp"/>
	</bean>
```



3. web.xml

   웹.xml에 서블릿을 추가해주는 태그를 달아준다. 이때 서블릿 이름은 2번의 파일 이름 앞쪽과 같아야한다.

   ```
   <servlet>
   		<servlet-name>springapp</servlet-name>
   		<servlet-class>
   			org.springframework.web.servlet.DispatcherServlet
   		</servlet-class>
   	</servlet>
   	
   	<servlet-mapping>
   		<servlet-name>springapp</servlet-name>
   		<url-pattern>*.do</url-pattern>
   	</servlet-mapping>
   ```

   

4. 컨트롤러 생성

   컨트롤러를 생성해주는데 @Controller 어노테이션을 달아줘서 컨트롤러라는걸 명시해준다.

   내부에 메서드에는 @RequestMapping() 어노테이션을 이용해서 url을 매핑해준다.

   뷰를 연결시켜주는것은 ModelAndView를 이용해서 연결해준다.

```
@Controller
public class HelloController {
	
	@RequestMapping("/hello.do")
	public ModelAndView hello(){
		//1. 비지니스로직 호출
		//2. 데이터를 저장
		//3. 뷰를 결정
		ModelAndView mav = new ModelAndView();
		mav.addObject("message","Hello Spring!!!");
		mav.setViewName("hello");
		
		return mav;
	}
}
```



이렇게 작성해주고 JSP나 HTML 파일을 만들어두면 서블릿 컨트롤러를 통해 뷰가 브라우저로 반환된다.

