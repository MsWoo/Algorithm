class Solution {
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        boolean[][] visited = new boolean[m][n];
        
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(picture[i][j] > 0 && !visited[i][j]){
                    numberOfArea++;
                    visited[i][j] = true;
                    
                    int cnt = 1;
                    cnt = find(i, j, cnt, picture, visited);
                    
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, cnt);
                }
            }
        }
        
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        
        return answer;
    }
    
    public int find(int x, int y, int cnt, int[][] picture, boolean[][] visited){
        int[] dxs = {1, -1, 0, 0};
        int[] dys = {0, 0, 1, -1};
        
        for(int i=0;i<4;i++){
            int nx = x + dxs[i];
            int ny = y + dys[i];
            
            if(nx < 0 || nx >= picture.length || ny < 0 || ny >= picture[0].length || visited[nx][ny]){
                continue;
            }
            
            if(picture[x][y] == picture[nx][ny]){
                visited[nx][ny] = true;
                cnt++;
                cnt = find(nx, ny, cnt, picture, visited);
            }
        }
        
        return cnt;
    }
    
}