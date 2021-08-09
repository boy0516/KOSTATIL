package kosta.io;

public class FileExam{
    
    public static void fileList(File file){
        if(file.isDirectory()){
            File[] files = file.listFiles();
            for(int i = 0; i<files.length; i++){
                fileList(files[i])
                System.out.println("이름:"+ files[i].getName());
            }
        }else{
            System.out.println("이름:" + file.getName());
        }
    }

    public static void show(FIle file){
        if(file.isDirectory()){
            File[] files = file.listFiles();
            for(int i = 0; i<files.length; i++){
                System.out.println("이름:"+ files[i].getName());
            }
        }else{
            System.out.println("이름:" + file.getName());
        }
    }

    public static void main(String[] args){
        String path = "D:\\223\\Java";
        File f = new File(path);
        show(f);
        show(new File("D:\\223\\Java", "객체내용.txt"));
    }
}

