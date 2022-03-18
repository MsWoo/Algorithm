class Solution {
    public int solution(String s) {
        int answer = 1000;
        
        for(int i=1;i<=s.length();i++){
            String temp = "";
            
            String std = s.substring(0,i);
            String mod = s.substring(i);
            
            int cnt = 1;
            
            for(int j=0;j<Math.ceil((s.length()-i)/i);j++){
                String cur = mod.substring(0,i);
                mod = mod.substring(i);
                
                if(std.equals(cur)){
                    cnt++;
                }
                else{
                    if(cnt != 1){
                        temp += Integer.toString(cnt);
                    }
                    temp += std;
                    std = cur;
                    cnt = 1;
                }
                                
            }
            if(cnt != 1){
                temp += Integer.toString(cnt);
            }
            temp += std;
            temp += mod;
            
            answer = Math.min(answer, temp.length());
            
        }
        
        return answer;
    }
}