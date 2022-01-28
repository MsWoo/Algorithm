import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;

        ArrayList<Integer> list = new ArrayList<>();
        
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                for(int k=j+1;k<nums.length;k++){
                    int num = nums[i] + nums[j] + nums[k];
                    if(check(num)){
                        answer++;
                    }
                }
            }
        }
        return answer;
    }
    
    public boolean check(int num){
        for(int i=2;i<num;i++){
            if(num%i==0){
                return false;
            }
        }
        return true;
    }
}