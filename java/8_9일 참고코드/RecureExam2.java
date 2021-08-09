package kosta.io;

public class FileExam{

    public static void recur(int n){
        if(n==0){
            return 0;
        }else{
            return n + recur(n-1)
        }
    }

    public static void recur2(int n,int[] arr){
        if(n==0 ){
            return 0;
        }else{
            return arr[n-1] + recur(n-1,arr)
        }
    }
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.println("입력");
        int n = sc.nextInt();
        int arr[] = {10,20,30,40,50,60,70,80,90}

        System.out.println(recur2());
        

        
    }
}
