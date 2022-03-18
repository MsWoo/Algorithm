class Solution {
    public int solution(int m, int n, String[] board) {
        int answer = 0;
        int retval;
        
        char[][] charBoard = new char[m][n];
        boolean[][] visited = new boolean[m][n];
        
        for(int i=0;i<board.length;i++){
            char[] temp = board[i].toCharArray();
            for(int j=0;j<temp.length;j++){
                charBoard[i][j] = temp[j];
            }
        }
        
        while(true){
            find4Block(m, n, charBoard, visited);
            retval = dropBlock(m, n, charBoard, visited);
            
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    visited[i][j] = false;
                }
            }
            
            if(retval != 0) answer += retval;
            else break;
        }
        
        return answer;
    }
    
    public void find4Block(int m, int n, char[][] charBoard, boolean[][] visited){
        for(int i=0;i<m-1;i++){
            for(int j=0;j<n-1;j++){
                if(charBoard[i][j] == '*') continue;
                
                if(charBoard[i][j] == charBoard[i][j+1] &&
                  charBoard[i][j] == charBoard[i+1][j] &&
                  charBoard[i][j] == charBoard[i+1][j+1]){
                    visited[i][j] = true;
                    visited[i][j+1] = true;
                    visited[i+1][j] = true;
                    visited[i+1][j+1] = true;
                }
            }
        }
    }
    
    public int dropBlock(int m, int n, char[][] charBoard, boolean[][] visited){
        int cnt = 0;
        
        for(int i=m-1;i>=0;i--){
            for(int j=0;j<n;j++){
                if(visited[i][j]){
                    cnt++;
                    charBoard[i][j] = '*';
                    
                    int new_i = i-1;
                    while(true){
                        if(new_i < 0)
                            break;
                        
                        if(visited[new_i][j]){
                            charBoard[new_i][j] = '*';
                        } 
                        else{
                            charBoard[i][j] = charBoard[new_i][j];
                            charBoard[new_i][j] = '*';
                            
                            visited[new_i][j] = true;
                            cnt--;
                            break;
                        }
                        new_i--;
                    }
                }
            }
        }
        
        return cnt;
    }
    
}