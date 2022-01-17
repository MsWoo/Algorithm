import java.util.*;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = {};
        
        ArrayList<String> list1 = new ArrayList<>();
        ArrayList<String> list2 = new ArrayList<>();
        
        for(int i=0;i<n;i++){
            String bin = Integer.toBinaryString(arr1[i]);
            String bin2 = Integer.toBinaryString(arr2[i]);
            
            while(bin.length()<n){
                bin = "0" + bin;
            }
            while(bin2.length()<n){
                bin2 = "0" + bin2;
            }
            list1.add(bin);
            list2.add(bin2);
        }
        
        answer = new String[n];
        
        for(int i=0;i<n;i++){
            String temp = "";
            String[] str1 = list1.get(i).split("");
            String[] str2 = list2.get(i).split("");
            for(int j=0;j<n;j++){
                if(str1[j].equals('1') || str2[j].equals("1")){
                    temp += "#";
                }
                else if(str1[j].equals("0") && str2[j].equals("0")){
                    temp += " ";
                }
                else{
                    temp += "#";
                }
            }
            
            answer[i] = temp;
        }
        
        return answer;
    }
}