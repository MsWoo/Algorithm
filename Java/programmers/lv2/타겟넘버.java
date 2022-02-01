class Solution {
    int answer = 0;
    
    public int solution(int[] numbers, int target) {
        dfs(0, target, 0, numbers);
        return answer;
    }
    
    public void dfs(int depth, int target, int sum, int[] numbers){
        if(depth == numbers.length){
            if(target == sum)
                answer++;
        }
        else{
            dfs(depth+1, target, sum+numbers[depth], numbers);
            dfs(depth+1, target, sum-numbers[depth], numbers);
        }
    }
}