# 스프링에서 RESTful

@PathVariable을 이용해서 URL의 데이터를 가져다 쓸 수 있다.

```
@RequestMapping("/board_detail{seq}")	
	public String board_detail(@PathVariable int seq, Model model){
		Board board = dao.detailBoard(seq);
		//데이터 저장
		model.addAttribute("seq", seq);
		model.addAttribute("detail",board);
		
		return "detail";
	}
```

이런식으로 @PathValiable을 이용해서 URL의 앞에서 부터 하나씩 가져다 쓴다.

