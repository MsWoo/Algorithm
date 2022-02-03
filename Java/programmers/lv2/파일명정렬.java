class Solution {
    String curHead, nextHead;
    int curNum, nextNum;
    
    public String[] solution(String[] files) {
        String[] answer = new String[files.length];
        String temp;
        
        for(int i=1;i<files.length;i++){
            for(int j=0;j<files.length-i;j++){
                
                splitHead(files[j], files[j+1]);
                splitNumber(files[j], files[j+1]);
                        
                if(curHead.compareTo(nextHead) > 0){
                    temp = files[j+1];
                    files[j+1] = files[j];
                    files[j] = temp;
                }
                else if(curHead.compareTo(nextHead) == 0){
                    if(curNum > nextNum){
                        temp = files[j+1];
                        files[j+1] = files[j];
                        files[j] = temp;
                    }
                }
            }
        }
        
        for(int i=0;i<files.length;i++){
            answer[i] = files[i];
        }
        
        return answer;
    }
    
    public void splitHead(String file, String file2){
        String[] temp = file.split("[0-9]+");
        curHead = temp[0].toLowerCase();
        
        temp = file2.split("[0-9]+");
        nextHead = temp[0].toLowerCase();
    }
    
    public void splitNumber(String file, String file2){
        String temp = file.substring(curHead.length());
        String num = "";
        for(char c : temp.toCharArray()){
            if(Character.isDigit(c) && num.length() < 5){
                num += c;
            }
            else break;
        }
        curNum = Integer.parseInt(num);
        
        temp = file2.substring(nextHead.length());
        num = "";
        for(char c : temp.toCharArray()){
            if(Character.isDigit(c) && num.length() < 5){
                num += c;
            }
            else break;
        }
        nextNum = Integer.parseInt(num);
    }
    
}