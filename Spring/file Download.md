# file Download

다운로드를 위해서 객체를 view로 이용해서 파일을 다운로드할 수 있도록 할것이다.

객체를 빈으로 등록한다.



이렇게 등록해준다.

`<bean id="downloadView" class="kosta.view.DownloadView"/>`



객체를 뷰로 이용하려면 새로운 viewResolver가 필요하다. 

```
<bean id="viewResolver3" class="org.springframework.web.servlet.view.BeanNameViewResolver"></bean>
```

이렇게 bean을 view로 이용할 수 있는 viewResolver를 생성해준다.



컨트롤러에는 다음과 같이 넣어준다.

```
@RequestMapping("/board_download")
	public String board_download(@RequestParam("filename") String filename, Model model)throws Exception{
		
		File file = new File(uploadDir, filename);
		model.addAttribute("downloadFile", file);
		return "downloadView";
	}
```

