# validator

```
<!-- https://mvnrepository.com/artifact/org.hibernate/hibernate-validator -->
<dependency>
    <groupId>org.hibernate</groupId>
    <artifactId>hibernate-validator</artifactId>
    <version>4.3.2.Final</version>
</dependency>

```





### JSR303

https://programmingrecoding.tistory.com/33



## 이용 예시

![image-20211103121845545](assets\image-20211103121845545.png)

이런 느낌으로 validation 제약을 걸어준다.

그리고 

![image-20211103121957651](assets\image-20211103121957651.png)

이렇게 컨트롤러에서 @Valid 를 통해 Validation을 진행하고 문제가 발생하면 BindingResult를 이용해서 errors를 생성한다.

errors.hasErrors()를 이용해서 에러 발생여부를 판단할 수 있다.



### Validation 실패했을때 페이지에 다시 정보를 띄워줄떄

controller 에서 form으로 데이터를 전달해야한다. 

이때 쓰는게 

@ModelAttribute 이다.

그러면 에러메시지와 폼에서 작성한 내용을 다시 반환해준다.

![image-20211103124747096](assets\image-20211103124747096.png)

3번째 줄과 같이 삽입해준다.

