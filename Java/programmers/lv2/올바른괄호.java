class Solution {
    boolean solution(String s) {
        int left = 0;
        int right = 0;
        
        for(int i=0;i<s.length();i++){
            if(right > left)
                return false;  
            
            if(s.charAt(i) == '(')
                left++;
            else
                right++;
        }

        return (left == right) ? true : false;
    }
}