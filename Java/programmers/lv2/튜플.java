import java.util.*;

class Solution {
    public ArrayList<Integer> solution(String s) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        s = s.substring(2, s.length()-2).replace("},{", "-");
        
        String[] strs = s.split("-");
        Arrays.sort(strs, new Comparator<String>(){
            public int compare(String o1, String o2){
                return Integer.compare(o1.length(), o2.length());
            }
        });

        for(String str : strs){
            String[] temp = str.split(",");
            for(int i=0;i<temp.length;i++){
                if(!answer.contains(Integer.parseInt(temp[i])))
                    answer.add(Integer.parseInt(temp[i]));
            }
        }
        
        return answer;
    }
}