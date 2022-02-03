class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int a, b;
        
        for(int i=1;i<=yellow;i++){
            if(yellow%i != 0){
                continue;
            }
            
            a = ((yellow/i)+2)*2;
            b = (i*2);
            
            if(a+b == brown){
                answer[0] = (yellow/i)+2;
                answer[1] = i+2;
                break;
            }
        }
        
        return answer;
    }
}