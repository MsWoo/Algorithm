import java.util.*;
class Solution {
    public int solution(String name) {
        int answer = 0;
        int len = name.length();
        int min = len - 1;
        
        for(int i=0;i<len;i++){
            char c = name.charAt(i);
            answer += (c - 'A' < 'Z' - c + 1) ? (c - 'A') : ('Z' - c + 1);
            
            int next = i+1;
            
            while(next < len && name.charAt(next) == 'A')
                next++;
            
            min = Math.min(min, (i*2)+len-next);
            min = Math.min(min, (len-next)*2+i);
        }
        
        answer += min;
        
        return answer;
    }
}