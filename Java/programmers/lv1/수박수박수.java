class Solution {
    public String solution(int n) {
        String answer = "";  
        int i = 0;
        
        while (i < n){
            answer += (i%2==0) ? "수" : "박";
            i++;
        }
        
        return answer;
    }
}