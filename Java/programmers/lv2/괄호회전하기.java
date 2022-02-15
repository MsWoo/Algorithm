import java.util.*;
class Solution {
    int answer = 0;
    
    public void check(String s){
        ArrayList<Character> left = new ArrayList<>(Arrays.asList( '(', '{', '[' ));
        ArrayList<Character> right = new ArrayList<>(Arrays.asList( ')', '}', ']' ));

        Stack<Character> stack = new Stack<>();
        
        if(right.indexOf(s.charAt(0)) >= 0)
            return;
        
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(!stack.isEmpty()){
                //left
                if(left.indexOf(c) >= 0)
                    stack.push(c);
                
                //right
                else{
                    if(left.indexOf(stack.peek()) == right.indexOf(c))
                        stack.pop();
                    else
                        return;
                }
            }
            else
                stack.push(c);
        }
        
        if(stack.isEmpty()) 
            answer++;
        
    }
    
    public int solution(String s) {
    
        check(s);
        
        for(int i=1;i<s.length();i++){
            s = s.substring(1,s.length()) + s.substring(0,1);
            check(s);
        }
        
        return answer;
    }
}