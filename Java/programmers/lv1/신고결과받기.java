import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        
        Map<String, Integer> result = new LinkedHashMap<>();
        
        Map<String, ArrayList<String>> reportMap = new HashMap<>();
        
        HashSet<String> temp = new HashSet<>(Arrays.asList(report));
        String[] reports = temp.toArray(new String[0]);
        
        for (int i=0;i<id_list.length;i++){
            result.put(id_list[i], 0);
            ArrayList<String> list = new ArrayList<>();
            reportMap.put(id_list[i], list);
        }
        
        for (int i=0;i<reports.length;i++){
            String[] arr = reports[i].split(" ");
            String reporter = arr[0];
            String target = arr[1];
            
            if (reportMap.containsKey(target)){
                reportMap.get(target).add(reporter);
            }
            
        }
        
        for (String key : reportMap.keySet()){
            if (reportMap.get(key).size() >= k){
                for(String i : reportMap.get(key)){
                    result.put(i, result.get(i)+1);
                }
            }
        }
        
        return result.values().stream().mapToInt(Integer::intValue).toArray();

    }
}