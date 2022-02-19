import java.util.*;
class Solution {
    
    class Task{
        int loc;
        int pri;
        public Task(int loc, int pri){
            this.loc = loc;
            this.pri = pri;
        }
    }  
    
    public int solution(int[] priorities, int location) {
        int answer = 0;

        Queue<Task> queue = new LinkedList<>();
        
        for(int i=0;i<priorities.length;i++){
            queue.add(new Task(i, priorities[i]));
        }
        
        int idx = 0;
        while(!queue.isEmpty()){
            Task cur = queue.poll();
            boolean flag = false;
            for(Task t : queue){
                if(cur.pri < t.pri){
                    flag = true;
                }
            }
            
            if(flag){
                queue.add(cur);
            }
            else{
                idx++;
                if(cur.loc == location){
                    answer = idx;
                    break;
                }
            }
            
        }
        
        return answer;
    }
}