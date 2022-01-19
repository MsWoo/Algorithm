import java.util.*;

class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        
        int cur = 0;
        ArrayList<Integer> nums = new ArrayList<>();
        int[] scores = new int[3];
        
        for(int i=0;i<dartResult.length();i++){
            char c = dartResult.charAt(i);
            
            if(Character.isDigit(c)){
                if(c == '1' && dartResult.charAt(i+1) == '0'){
                    nums.add(10);
                    i++;
                }
                else{
                    nums.add(Character.getNumericValue(c));
                }
            }
            else{
                if(c == 'S'){
                    scores[cur] = (int) Math.pow(nums.get(cur), 1);
                    cur++;
                }
                else if(c == 'D'){
                    scores[cur] = (int) Math.pow(nums.get(cur), 2);
                    cur++;
                }
                else if(c == 'T'){
                    scores[cur] = (int) Math.pow(nums.get(cur), 3);
                    cur++;
                }
                else if(c == '*'){
                    if(cur < 2){
                        scores[0] *= 2;
                    }
                    else{
                        for(int j=cur-2;j<cur;j++){
                            scores[j] *= 2;
                        }
                    }
                }
                else{
                    scores[cur-1] *= -1;
                }
            }
            
        }

        for(int i=0;i<scores.length;i++){
            answer += scores[i];
            System.out.println(scores[i]);
        }

        return answer;
    }
}