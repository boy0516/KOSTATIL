package kosta.file;

import java.io.File;

public class Cdup{
    public static File cdUp(File source)throws Exception{
    	String name = "";
    	String[] arr = source.getName().split("\\");
    	for(int i = 0; i<arr.length-1;i++) {
    		name += arr[i];
    		//이게 디렉토리경로에서 맨 뒤경로 빼고 이름을 다시 만들어준거에요
    		
    	}
        File cdPath = new File(name);
        
        return cdPath;// 디렉토리 반환
        
    }
}