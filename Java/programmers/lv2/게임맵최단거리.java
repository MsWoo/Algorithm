import java.util.*;

class Solution {

    int[] dxs = {-1, 1, 0, 0};
    int[] dys = {0, 0, -1, 1};

    public int solution(int[][] maps) {
        int answer = 0;
        int[][] visited = new int[maps.length][maps[0].length];

        bfs(maps, visited);
        answer = visited[maps.length-1][maps[0].length-1];
        
        if(answer == 0)
            return -1;
        
        return answer;
    }
    
    public void bfs(int[][] maps, int[][] visited){
        visited[0][0] = 1;
        
        LinkedList<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0});
        
        while(!queue.isEmpty()){
            int[] xy = queue.remove();
            int x = xy[0];
            int y = xy[1];
            
            for(int i=0;i<4;i++){
                int nx = x + dxs[i];
                int ny = y + dys[i];
                
                if(nx < 0 || nx >= maps.length || ny < 0 || ny >= maps[0].length)
                    continue;
                
                if(visited[nx][ny] == 0 && maps[nx][ny] == 1){
                    visited[nx][ny] = visited[x][y] + 1;
                    queue.add(new int[]{nx, ny});
                }
            }
        } 
    }
    
}