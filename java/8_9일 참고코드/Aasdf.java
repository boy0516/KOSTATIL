package kosta.file;

import java.io.File;
import java.io.PrintStream;
import java.util.Scanner;

public class Aasdf {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String source = "E:\\jihuntest";
		Scanner sc = new Scanner(System.in);
		File nowPath = new File("source");
		String commend = sc.nextLine();
		String[] commendArr= commend.split(" ");// 여기 구분자요
		// cd 디렉토리명  이게 명령어니까 이걸받아서 split해주면 될거가타요
		switch (commendArr[0]) {
		
		case "cd":
			//저는 .. 일때 실행되게해서 
			if (commendArr[1] =="..") {
				try {
					nowPath=Cdup.cdUp(nowPath);//메서드 불러오고요
				}catch(Exception e) {
					e.printStackTrace();
				}
				System.out.println(nowPath.getName());
			}
			
			
			break;
		

		default:
			break;
		}
	}

}
