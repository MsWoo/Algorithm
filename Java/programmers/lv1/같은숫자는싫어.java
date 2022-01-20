import java.util.*;

public class Solution {
    public int[] solution(int []arr) {

        ArrayList<Integer> ret = new ArrayList<>();
        int idx = 0;
        
        ret.add(arr[0]);
        idx++;
        
        for(int i=1;i<arr.length;i++){
            if(ret.get(idx-1) != arr[i]){
                ret.add(arr[i]);
                idx++;
            }
        }
        
        return ret.stream().mapToInt(i->i).toArray();
        
//         Set<Integer> set = new LinkedHashSet<>();
        
//         for(int ele : arr){
//             set.add(ele);
//         }
        
//         Integer[] array = set.toArray(new Integer[0]);

//         return Arrays.stream(array).mapToInt(Integer::intValue).toArray();
    }
}