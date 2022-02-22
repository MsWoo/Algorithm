import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
       
        ArrayList<String> list = new ArrayList<>();       
        
        String cur = words[0];
        list.add(cur);
        
        for(int i=1;i<words.length;i++){  
              
            if((cur.charAt(cur.length()-1) != words[i].charAt(0)) || list.contains(words[i])){
                answer[0] = i%n+1;
                answer[1] = i/n+1;
                break;
            }
            
            cur = words[i];
            list.add(cur);    
        }

        return answer;
    }
}