package kosta.io;

public class CopyUtil{

    //복사 대상 폴더(디렉토리) Copy구현(새로운 디렉토리 생성 후 그 안에 모든 파일을 복사)
    public static void copyDirectory(File source, File dest)throws Exception{

        if(source.isDirectory()){
            dest.mkdir();

            File[] files = source.listFiles();
            for(int i = 0; i<files.length; i++){
                File sourceFile = new FileList[i];
                if(sourceFile.isDirectory()){
                    File s_destFile = new File(dest, sourceFile.getName());
                    copyDirectory(sourceFile, s_destFile)
                }else{
                    File destFile = new File(dest, sourceFile.getName());
                    copyFile(sourceFile,destFile);
                }
                

            }
        }else{
            copyFile(File source, File dest)
        }


    }
    public static void copyFile(File source, File dest)throws Exception{
        FileOutputStream out = null;
		FileInputStream in = null;
        byte[] arr = new byte[500];
        int data = 0;

        try {
			in = new FileInputStream(source);
            out = new FileOutputStream(dest);
			
			while((data = in.read(arr)) != -1) {
				out.write(arr);
                Arrays.fill(arr,(byte)0);
			}
			
		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("실패");
		}finally {
			try {
                if(in != null){
                    in.close();
                }
                if(out != null){
                    out.close();
                }
			} catch (Exception e2) {
				// TODO: handle exception
			}
		} 
    }
}