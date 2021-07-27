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

		int N = Integer.parseInt(st.nextToken());

		if(N<3 || N>5000)
			return;
		
		int count = 0;
		
		while(N>0) {
			if(N%5 == 0) {
				N -= 5;
				count++;
			}
			else if(N%3 == 0) {
				N -= 3;
				count++;
			}
			else if(N > 5) {
				N -= 5;
				count++;
			}
			else {
				count = -1;
				break;
			}
		}
		System.out.println(count);
		
	}
}