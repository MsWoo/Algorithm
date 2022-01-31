import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        int[] answer = {};
        
        Map<String, String> inTime = new HashMap<>();
        Map<String, Integer> count = new HashMap<>();
        Map<String, Integer> result = new HashMap<>();
        
        for(String s : records){
            String[] record = s.split(" ");
            
            //In
            if (record[2].equals("IN")){
                inTime.put(record[1], record[0]);
                
                //Count 입차
                if(count.get(record[1]) == null){
                    count.put(record[1], 1);
                }
                else{
                    count.put(record[1], count.get(record[1])+1);
                }
                
                
            }
            //Out
            else{
                //Count 출차
                count.put(record[1], count.get(record[1])+1);
                
                //사용시간 계산
                int usingTime = calcul(inTime.get(record[1]), record[0]);
                
                //result에 담기
                if(result.get(record[1]) == null){
                    result.put(record[1], usingTime);
                }
                else{
                    result.put(record[1], result.get(record[1]) + usingTime);
                }
                
                
            }  
        }
        
        //출차안한것 처리
        Set<String> keySet = count.keySet();
        for(String key : keySet){
            if(count.get(key) % 2 == 1){
                if(result.get(key) == null){
                    result.put(key, calcul(inTime.get(key), "23:59"));
                }
                else{
                    result.put(key, result.get(key) + calcul(inTime.get(key), "23:59"));
                }
            }
        }
        
        //key기준 sort
        Object[] resultKey = result.keySet().toArray();
        Arrays.sort(resultKey);
        answer = new int[resultKey.length];
        
        //총요금 계산
        for(int i=0;i<resultKey.length;i++){
            double t = result.get(resultKey[i]);
            answer[i] += fees[1];
            
            if(t > fees[0]){
                answer[i] += (int) Math.ceil((t - fees[0]) / fees[2]) * fees[3];
            }
        }

        return answer;
    }
    
    public int calcul(String a, String b){
        String[] start = a.split(":");
        String[] end = b.split(":");
        int result = 0;
        
        result += (Integer.parseInt(end[0]) - Integer.parseInt(start[0])) * 60;
        result += Integer.parseInt(end[1]) - Integer.parseInt(start[1]);
        
        return result;
    }
    
}