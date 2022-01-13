import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        String[] cs = s.split("");
        Arrays.sort(cs);
        
        for (int i=cs.length-1;i>=0;i--){
            answer += cs[i];
        }
        
        return answer;
    }
}