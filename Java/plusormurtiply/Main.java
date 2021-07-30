package test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		String N = st.nextToken();
		String[] array = N.split("");
		
		int result = 0;
		
		int[] arr = new int[array.length];
		
		for(int i=0;i<array.length;i++) {
			arr[i] = Integer.parseInt(array[i]);
		}

		for(int i=0;i<arr.length;i++) {
			if(arr[i] <= 1 || result <= 1)
				result += arr[i];
			else
				result *= arr[i];
		}
		
		System.out.println(result);
		
	}
}