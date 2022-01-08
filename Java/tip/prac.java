import java.util.*;

class Solution {
    public int solution(int[] A) {

        ArrayList<Integer> list = new ArrayList<>();
        ArrayList<Integer> neg_list = new ArrayList<>();
        int temp;
        int cnt = 0;

        for(int ele : A){
            list.add(ele);
        }

        while(true){
            temp = 0;
            
            for(int i=0;i<list.size();i++){
                temp += list.get(i);
                if (list.get(i) < 0)
                    neg_list.add(list.get(i));

                if (temp < 0) {
                    neg_list.sort(null);
                    int idx = list.indexOf(neg_list.get(0));
                    list.remove(idx);
                    list.add(neg_list.get(0));
                    neg_list.clear();
                    cnt += 1;
                    break;
                }

                if (i == list.size()-1) {
                    return cnt;
                }
            }
        }
    }
}
