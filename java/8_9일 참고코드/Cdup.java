package kosta.file;

import java.io.File;

public class Cdup{
    public static File cdUp(File source)throws Exception{
    	String name = "";
    	String[] arr = source.getName().split("\\");
    	for(int i = 0; i<arr.length-1;i++) {
    		name += arr[i];
    		//�̰� ���丮��ο��� �� �ڰ�� ���� �̸��� �ٽ� ������ذſ���
    		
    	}
        File cdPath = new File(name);
        
        return cdPath;// ���丮 ��ȯ
        
    }
}