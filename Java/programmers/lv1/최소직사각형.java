import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        int n = sizes.length;

        int[][] resizes = new int[n][2];
        
        int maxX = 0, maxY = 0;
        
        for(int i=0;i<n;i++){
            resizes[i][0] = Math.max(sizes[i][0], sizes[i][1]);
            resizes[i][1] = Math.min(sizes[i][0], sizes[i][1]);
        }
        
        maxX = resizes[0][0];
        maxY = resizes[0][1];
        
        for(int i=1;i<n;i++){
            if(maxX < resizes[i][0])
                maxX = resizes[i][0];
            if(maxY < resizes[i][1])
                maxY = resizes[i][1];
        }
        
        
        answer = maxX * maxY;
        
        return answer;
    }
}