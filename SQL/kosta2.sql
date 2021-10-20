
CREATE TABLE users(
	user_num NUMBER PRIMARY KEY,
	user_name VARCHAR2(1000) NOT NULL,
	user_phoneNum VARCHAR2(1000) NOT NULL,
	user_email VARCHAR2(1000) NOT NULL,
	user_pw VARCHAR2(1000) NOT NULL,
	user_birth VARCHAR2(1000) NOT NULL,
	user_pwHint VARCHAR2(1000) NOT NULL
);

CREATE SEQUENCE user_num;

CREATE TABLE team(
	team_num NUMBER PRIMARY KEY,
	team_name VARCHAR2(100) NOT NULL,
	team_info VARCHAR2(100),
	user_num NUMBER REFERENCES users(user_num)
);

CREATE SEQUENCE team_num;


CREATE TABLE members(
	member_num NUMBER PRIMARY KEY,
  member_position VARCHAR2(1000) NULL,
  team_num NUMBER REFERENCES team(team_num),
  user_num NUMBER REFERENCES users(user_num)
 );

CREATE SEQUENCE member_num;


CREATE TABLE boards(
	board_num NUMBER PRIMARY KEY,
	board_name VARCHAR2(1000) NOT NULL,
	board_info VARCHAR2(1000),
	team_num NUMBER REFERENCES team(team_num),
	member_num NUMBER REFERENCES members(member_num)
);

CREATE SEQUENCE board_num;

CREATE TABLE chatRoom(
	chatroom_num NUMBER PRIMARY KEY,
	chatroom_name VARCHAR2(1000) NOT NULL,
	git_token VARCHAR2(1000),
	team_num REFERENCES team(team_num)
);

CREATE SEQUENCE chatroom_num;

CREATE TABLE chat(
	chat_num NUMBER PRIMARY KEY,
	chat_contents VARCHAR2(1000) NOT NULL,
  	chat_uploadFile VARCHAR2(1000) NULL,
	chatroom_num REFERENCES chatRoom(chatroom_num),
  	member_num REFERENCES members(member_num) 
 );

CREATE SEQUENCE chat_num;

CREATE TABLE chatMember(
	chatroom_num NUMBER NOT NULL,
	member_num NUMBER NOT NULL
);

--foreign key설정
ALTER TABLE chatMember
		ADD CONSTRAINT chatMember_chatroom_num_fk
		FOREIGN KEY (chatroom_num)
		REFERENCES chatroom(chatroom_num);

--foreign key설정
ALTER TABLE chatMember
		ADD CONSTRAINT chatMember_member_num_fk
		FOREIGN KEY (member_num)
		REFERENCES members(member_num);


CREATE TABLE post(
	post_num NUMBER PRIMARY KEY,
	post_title VARCHAR2(1000),
	post_contents VARCHAR2(1000),
	board_num NUMBER REFERENCES boards(board_num),
	member_num NUMBER REFERENCES members(member_num)	
);


CREATE TABLE comments(
	comment_num NUMBER NOT NULL,
	comment_contents VARCHAR(1000) NOT NULL,
	member_num NUMBER NOT NULL,
	post_num NUMBER NOT NULL
);

--primary키 설정 
ALTER TABLE comments 
		ADD CONSTRAINT comments_comment_num_pk PRIMARY KEY(comment_num);

--foreign key
ALTER TABLE comments
		ADD CONSTRAINT comments_member_num_fk
		FOREIGN KEY (member_num)
		REFERENCES member(member_num);

--foreign key
ALTER TABLE comments
		ADD CONSTRAINT comments_post_num_fk
		FOREIGN KEY (post_num)
		REFERENCES post(post_num);
CREATE TABLE calendar(
	calendar_num NUMBER NOT NULL,
	team_num NUMBER NOT NULL
);
--ALTER pk 설정
ALTER TABLE calendar
		ADD CONSTRAINT calendar_calendar_num_pk PRIMARY KEY(calendar_num);

--ALTER FK 설정
ALTER TABLE calendar
		ADD CONSTRAINT calendar_calendar_num2_pk
		FOREIGN KEY (team_num)
		REFERENCES team(team_num);
    
    
CREATE SEQUENCE comment_num;
CREATE SEQUENCE post_num;