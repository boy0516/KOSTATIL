# file UPLOAD

1. pom.xml

   -commons-io, commons-fileupload

```
<dependency>
			<groupId>commons-io</groupId>
			<artifactId>commons-io</artifactId>
			<version>2.8.0</version>
		</dependency>
		<!-- https://mvnrepository.com/artifact/commons-fileupload/commons-fileupload -->
		<dependency>
			<groupId>commons-fileupload</groupId>
			<artifactId>commons-fileupload</artifactId>
			<version>1.4</version>
		</dependency>
```

2. insert_form.jsp -> form추가

```
<form:form action="board_insert" method="post" commandName="boardCommand" enctype="multipart/form-data">
	작성자 : <form:input type="text" path="writer"/>
			<form:errors path="writer" cssClass="error"/><br>
	제목 : <form:input type="text" path="title"/>
			<form:errors path="title" cssClass="error"/><br>
	파일:<input type="file" name="uploadFile"/><br>				
	내용 <br>
	<form:textarea rows="6" cols="70" path="contents"></form:textarea>
	<br>
	<input type="submit" value="등록">
</form:form>
```

위코드에서 파일 부분과 form태그의 enctype을 추가해준다.

```

enctype="multipart/form-data"

파일:<input type="file" name="uploadFile"/><br>	

```

이렇게 두가지 



3. 

```java
MultipartFile multipartFile = board.getUploadFile();
		//multipartFile.getOriginalFilename() 이거는 파일이름을 추출하는 메서드
		if(multipartFile.getOriginalFilename() != null && multipartFile.getOriginalFilename().length() != 0){
			String fname = multipartFile.getOriginalFilename();
			board.setFname(fname);
			
			try{
				//여기서 변환이 이루어져서 파일이 해당 경로로 저장이 된다.
				multipartFile.transferTo(new File(uploadDir, fname));
			}catch(Exception e){
				e.printStackTrace();
			}
		}
```





정리하자면 multipart로 파일을 받으려면 servlet.xml에 

```
<!-- File Up/Down Setting -->
	
<bean id="multipartResolver" class="org.springframework.web.multipart.commons.CommonsMultipartResolver">
		<property name="defaultEncoding" value="UTF-8"/>
</bean>
```

이걸 넣어줘서 multipartResolver를 넣어주고



그 다음은 jsp에서는 form에

```
enctype="multipart/form-data"
```

이걸 넣어줘서 multipart로 받는다는걸 명시해주고

```
파일:<input type="file" name="uploadFile"/><br>	
```

파일을 업로드 하면 컨트롤러에서 받아줘야한다.

멀티파트파일로 보드객체에 저장되어있는 파일을 받아오고

```
MultipartFile multipartFile = board.getUploadFile();
```

받아온 파일의 이름을 추출해서 저장하는 파일의 이름을 지정해준다.

```
//multipartFile.getOriginalFilename() 이거는 파일이름을 추출하는 메서드
```

```
if(multipartFile.getOriginalFilename() != null && multipartFile.getOriginalFilename().length() != 0){
			String fname = multipartFile.getOriginalFilename();
			board.setFname(fname);
			
			try{
				//여기서 변환이 이루어져서 파일이 해당 경로로 저장이 된다.
				multipartFile.transferTo(new File(uploadDir, fname));
			}catch(Exception e){
				e.printStackTrace();
			}
		}
```

위 코드에서 멀티파트파일의 이름이 존재하면 로직이 실행되는 if문이 있고 

그 아래에는 파일 이름을 받아주고 그 이름으로 파일을 생성해준다.

`String fname = multipartFile.getOriginalFilename();` 이름 추출

`multipartFile.transferTo(new File(uploadDir, fname));`멀티파트파일 생성

