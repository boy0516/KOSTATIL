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
		String[] commendArr= commend.split(" ");// ���� �����ڿ�
		// cd ���丮��  �̰� ��ɾ�ϱ� �̰ɹ޾Ƽ� split���ָ� �ɰŰ�Ÿ��
		switch (commendArr[0]) {
		
		case "cd":
			//���� .. �϶� ����ǰ��ؼ� 
			if (commendArr[1] =="..") {
				try {
					nowPath=Cdup.cdUp(nowPath);//�޼��� �ҷ������
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
