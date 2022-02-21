import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int cur = 0;
        Queue<Integer> queue = new LinkedList<Integer>();
        
        for(int truck : truck_weights){
            
            while(true){
                if(queue.size() == bridge_length){
                    cur -= queue.poll();
                }
                
                if(cur + truck <= weight){
                    queue.add(truck);
                    cur += truck;
                    answer++;
                    break;
                }
                else{
                    queue.add(0);
                    answer++;
                }
            }
        }
        
        return answer + bridge_length;
    }
}