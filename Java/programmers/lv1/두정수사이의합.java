class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        if(a>b){
            int temp = a;
            a = b;
            b = temp;
        }
        int i = a;
        for(i=a;i<=b;i++){
            answer += i;
        }
        return answer;
    }
}