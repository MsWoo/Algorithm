import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(int ele : scoville){
            heap.offer(ele);
        }
               
        while(heap.peek() < K){
            if(heap.size() < 2)
                return -1;
            
            int f1 = heap.poll();
            int f2 = heap.poll();
            
            heap.offer(f1 + f2 * 2);
            answer++;
        }

        return answer;
    }

}