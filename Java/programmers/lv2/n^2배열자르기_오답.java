class Solution {
    public int[] solution(int n, long left, long right) {   
        int l = (int) left;
        int r = (int) right;
        
        int[] answer = new int[r-l+1];
        int[][] arrays = new int[n][n];
        
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                if(i<j)
                    arrays[i-1][j-1] = j;
                else
                    arrays[i-1][j-1] = i;
            }
        }
        
        int size = (int) Math.pow(n, 2);
        int[] temp = new int[size];
        int idx=0;
        
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                temp[idx++] = arrays[i][j];
            }
        }

        idx = 0;
        for(int i=l;i<+1;i++){
            answer[idx++] = temp[i];
        }
        
        return answer;
    }
}