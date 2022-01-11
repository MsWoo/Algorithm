class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        for (int ele : arr){
            answer += ele;
        }
        return answer/arr.length;
    }
}