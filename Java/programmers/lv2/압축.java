import java.util.*;

class Solution {
    public int[] solution(String msg) {
       
        //init
        ArrayList<Integer> answers = new ArrayList<>();
        Map<String, Integer> index = new LinkedHashMap<>();
        int idx = 27;
        
        for(int i=1;i<=26;i++){
            index.put(Character.toString((char)(64+i)), i);
        }
        
        char[] msgs = msg.toCharArray();
        
        //
        for(int i=0;i<msgs.length;i++){
            String w = Character.toString(msgs[i]);
            
            while(true){
                if(i+1 < msgs.length){
                    if(index.get(w + Character.toString(msgs[i+1])) == null){
                        String c = Character.toString(msgs[i+1]);
                        answers.add(index.get(w));
                        index.put(w+c, idx++);
                        break;
                    }
                    else{
                        w = w + Character.toString(msgs[i+1]);
                        i++;
                    }
                }
                else{
                    answers.add(index.get(w));
                    break;
                }
            }  
            
        }
        
        return answers.stream().mapToInt(i -> i).toArray();
    }
}