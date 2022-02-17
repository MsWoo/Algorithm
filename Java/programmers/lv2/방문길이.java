class Solution {
    public int solution(String dirs) {
        int answer = 0;
        boolean[][][] visited = new boolean[11][11][4];
        
        int x = 5;
        int y = 5;
        
        //LRUD
        int[] dxs = {0, 0, -1, 1};
        int[] dys = {-1, 1, 0, 0};
        
        for(char c : dirs.toCharArray()){
            int nx, ny, i;
            
            if(c == 'L') i = 0;
            else if(c == 'R') i = 1;
            else if(c == 'U') i = 2;
            else i = 3;
            
            nx = x + dxs[i];
            ny = y + dys[i];
            
            if(nx < 0 || nx > 10 || ny < 0 || ny > 10){
                continue;                
            }
            if(!visited[nx][ny][i]){
                visited[nx][ny][i] = true;
                i = (i%2 == 0) ? i+1 : i-1;
                visited[x][y][i] = true;

                answer++;
            }
            
            x = nx;
            y = ny;
        }
        
        return answer;
    }
}