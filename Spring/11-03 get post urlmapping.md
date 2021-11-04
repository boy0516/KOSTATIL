- DI - 명시적

```
  <bean id="helloController" class="kosta.controller.HelloController">	
  		<property name="service" ref="helloService"></property>
  </bean>
  <bean id="boardController" class="kosta.controller.BoardController"></bean>
  <bean id="helloService" class="kosta.service.HelloService"></bean>
```

- 자동

```
<context:annotation-config/>
<context:component-scan base-package="kosta"/>
```



아무튼 DI를 하기위해선

4가지중 하나는 선택해야한다.

@Controller, @Service, @Repository, @Conponent



index.html 요청 => urlmapping => "/" 모든 요청을 springMVC요청으로 인식

=> springMVC 찾을 수 없는 요청 404X => tomcat위임 요청하도록 함

```
springapp-servlet.xml에서 

<mvc:annotation-driven/>
	<mvc:default-servlet-handler/>
```

이걸 추가해준다.



- 같은 URL에서 메서드를 이용해서 리턴값을 구분하는 방법

  get방식과 post방식을 구분하겠다.

```
//	@RequestMapping(value="/board_insert", method=RequestMethod.GET)
	@GetMapping("/board_insert")
	public String insertForm(){
		return "insert_form";
	}
	
//	@RequestMapping(value="/board_insert", method=RequestMethod.POST)
	@PostMapping("/board_insert")
	public String board_insert(){
		System.out.println("board_insert POST 요청");
		return "";
	}
```

다음과 같이 **@GetMapping** **@PostMapping**을 구분해서 리턴값을 다르게 지정할 수 있다.



form에서 받아오는 컨트롤러로 전달할때 데이터를 객체로 바꿔주는 객체를 

BoardCommand 객체라고 한다.

또는 BoardDTO



그리고Service <---DB  디비에서 서비스로 가져오는것은 

BoardVO라고 한다. 이거는 왠만하면 이걸로 이름을 쓰자



