package kosta.homework;

import java.util.Scanner;

public class Work7_30 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int arr[] = new int[n];
		int count = 0;
		int num=0;
		
		for(int i =0; i<n; i++) {
			int num2 = sc.nextInt();
			if (num < num2) {
				count +=1;
				num = num2;
				
			}
	
		}
		System.out.println(count);
		
	}

}
