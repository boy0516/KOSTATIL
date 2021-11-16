팀 리스트 json
```json
[{
    "팀이름":"팀이름",
    "팀소유자이메일":"팀소유자이메일",
    "팀원사진URL":"URL",
},{
    "팀이름":"팀이름",
    "팀소유자이메일":"팀소유자이메일",
    "팀원사진URL":"URL",
},{
    "팀이름":"팀이름",
    "팀소유자이메일":"팀소유자이메일",
    "팀원사진URL":"URL",
}]
```



팀 생성하는 json

```JSON
{
	"팀이름":"팀이름",
    "팀설명":"팀설명",
    "세션에 들어있는 유저넘버":"유저넘버",
}
```



멤버검색하는데 쓰이는 JSON

```
selectAllUsers() 모든 유저 가져와서 json으로 만들어서 보내줌
```



멤버 추가하는 json

```json
{	
	"유저넘버":"유저넘버",
	"팀넘버":"팀넘버"
}
```



멤버 권한 수정하는 JSON

```json
{
    "member_position":"직책"
}
```



### RESTful API

#### team

get: /team  => 세션에 일치하는 팀 리스트 반환

get: /team/{team_num} => 팀 정보 반환

post: /team/new => 팀 생성 => 생성되면서 멤버에 삽입

put: /team/{team_num} =>팀 정보 수정

delete: /team/{team_num} => 팀 삭제

// ???post: /team/{team_num}/invite => 팀 초대  ( 겹치는거 같아서 삭제해야할듯)



#### members

get: /team/{team_num}/members=>팀번호에 맞는 멤버리스트 반환

get: /team/{team_num}/members/{member_num} =>멤버 정보 반환

post: /team/{team_num}/members/invite => 팀에 멤버 초대

put: /team/{team_num}/members/{member_num} =>멤버 정보 수정

delete: /team/{team_num}/members/{member_num} => 멤버 정보 삭제



```
<resultMap id="privacy" type="eventJoinUser">
    <result property="seq" column="SEQ" />
    <result property="privacySeq" column="PRIVACY_SEQ" />
    <result property="eventMasterSeq" column="EVENT_MASTER_SEQ" />
    <result property="eventMasterSeq" column="EVENT_MASTER_SEQ" />
    <result property="regDate" column="REG_DATE" />
    <result property="modDate" column="MOD_DATE" />
  
<!-- javaType : "객체를 속성으로 가지고있는 해당 객체의 CamelCase명 또는, @Alias("키값")" -->
<!-- property : "객체참조변수명" -->
<!-- id : "PK" -->
    <association property="privacyVo" javaType="privacy">
         <id property="seq" column="SEQ" />
         <result property="userName" column="USER_NAME" />
         <result property="phone1" column="PHONE1" />
         <result property="phone2" column="PHONE2" />
         <result property="phone3" column="PHONE3" />
    </association>
</resultMap>	
```

