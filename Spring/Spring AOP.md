# Spring AOP

- XML기반,  어노테이션기반
- 오늘은 어노테이션 기반으로 해보겠다.



- dependency

```
<!-- https://mvnrepository.com/artifact/org.springframework/spring-aspects -->
<dependency>
	<groupId>org.springframework</groupId>
	<artifactId>spring-aspects</artifactId>
	<version>4.3.2.RELEASE</version>
</dependency>
```



- springapp-servlet

```
<aop:aspectj-autoproxy/>

<bean id="sessionAspect" class="kosta.aspect.SessionAspect"/>
```

aop을 이용하기 위한 프록시를 지정해준다. 그리고 sessionAspect를 등록해준다.





Aspect 객체를 생성하고 어노테이션으로 명시해준다.

- @Aspect

그리고 공통관심사항 메서드에 @Around를 써서 메서드 종류를 명시해준다.

- @Around("execution(public * kosta.controller.*.*do(..))")

execution을 이용해서 pointcut을 지정해준다.



```
@Aspect
public class SessionAspect {
	
	@Around("execution(public * kosta.controller.*.*do(..))")
	public String sessionCheck(ProceedingJoinPoint joinPoint)throws Throwable{
		//세션유뮤를 체크 => Session객체
		Object[] obj = joinPoint.getArgs();
		HttpServletRequest request = (HttpServletRequest)obj[0];
		HttpSession session = request.getSession();
		
		String name = (String)session.getAttribute("name");
		String view = "session/session_fail";
		
		try{
			if(name== null){
				throw new Exception("no session");
			}
			
			view = (String)joinPoint.proceed();//session_do() 호출
			
		}catch(Exception e){
			return view;
		}
		
		return view;
	}
}
```



- SessionController.java

```
@Controller
public class SessionController {
	@RequestMapping("/session_req")
	public String session_req(){
		return "session/session_req";
	}
	
	@RequestMapping("/session_do")
	public String session_do(HttpServletRequest request){
		return "session/session_success";
	}
	
	@RequestMapping("/session_add")
	public String session_add(){
		return "session/session_add";
	}
}
```

여기에서 요청을 받아주는데 위의 AOP에 걸려서 세션체크로 넘어간다.

이때 session_do에 파라미터가 request가 있기때문에 이 파라미터가 Aspect로 넘어간다.



```
Object[] obj = joinPoint.getArgs();
HttpServletRequest request = (HttpServletRequest)obj[0];
HttpSession session = request.getSession();

String name = (String)session.getAttribute("name");
```

이런식으로 joinPoint의 Args를 통해서 첫번째 인자가 request로 전달된다.

