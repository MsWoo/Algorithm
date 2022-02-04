class Solution {
    public int solution(int n) {
        int num = n;
        
        while(true){
            if(Integer.bitCount(n) == Integer.bitCount(++num))
                break;    
        }
        
        return num;
    }
}