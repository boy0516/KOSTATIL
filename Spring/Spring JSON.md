# Spring JSON

pom.xml -> jackson 라이브러리 추가



Json컨트롤러 개발

@RestController 어노테이션으로 컨테이너에 저장



@RestController 안에 있는 RequestMapping 메서드들은 반환값에 객체를 넣으면 자동으로 JSON형식으로 데이터를 변환해서 반환해준다.



```
@RestController
public class JsonController {
	
	@Autowired
	private BoardDao dao;
	
	static List<Member> memberList = new ArrayList<>();
	
	static{
		memberList.add(new Member("홍길동",20,"서울"));
		memberList.add(new Member("박길동",20,"대구"));
		memberList.add(new Member("조길동",20,"부산"));
	}

	@RequestMapping("/member_list_json")
	public List<Member> member_list_json(){
		return memberList;
	}
	
	@PostMapping("member_save")
	public void member_save(@RequestBody Member m){
		memberList.add(m);
	}
	
	@RequestMapping("board_json")
	public Member member_json(@RequestParam("name") String name){
		Member m = null;
		for(int i = 0; i<memberList.size(); i++){
			if(memberList.get(i).getName().equals(name)){
				m = memberList.get(i);
				break;
			}
		}
		return m;
	}
	
	@RequestMapping("board_list_json")
	public List<Board> board_list_json(){
		return dao.list();
	}
}

```

![image-20211104152013352](assets\image-20211104152013352.png)

