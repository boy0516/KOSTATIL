## Validation 체크 후 ModelAttribute 반환

jsp에서도 form에서 수정이 필요하다.

먼저 jsp 맨위에 추가

```
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
```



```
<form:form action="board_insert" method="post" commandName="boardCommand">
	작성자 : <form:input type="text" path="writer"/>
			<form:errors path="writer" cssClass="error"/><br>
	제목 : <form:input type="text" path="title"/>
			<form:errors path="title" cssClass="error"/><br>					
	내용 <br>
	<form:textarea rows="6" cols="70" path="contents"></form:textarea>
	<br>
	<input type="submit" value="등록">
</form:form>
```

form태그 대신 form:form 태그를 써야한다.



스프링프레임워크의 JSP 기술중에 form taglib 가 있습니다. form 태그라이브러리를 사용하면 HTML 폼에 데이터를 바인딩하거나 에러메세지 처리등을 간편하게 할 수 있습니다.

출처: https://offbyone.tistory.com/325 [쉬고 싶은 개발자]

