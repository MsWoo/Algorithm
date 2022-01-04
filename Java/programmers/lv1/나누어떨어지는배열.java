import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = {};
        ArrayList<Integer> array = new ArrayList<Integer>();
        
        for(int i=0;i<arr.length;i++){
            if(arr[i]%divisor==0){
                array.add(arr[i]);
            }
        }
            
        if(array.isEmpty()){
            array.add(-1);
        }
            
        answer = new int[array.size()];
        
        for(int i=0;i<array.size();i++){
            answer[i] = array.get(i);
        }  
        
        Arrays.sort(answer);
        
        return answer;
    }   
}
