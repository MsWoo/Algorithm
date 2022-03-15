class Solution {
    public String solution(String msg, int N){
        String answer = "";
        int curSize = 0;

        String[] msgs = msg.split(" ");

		if(msgs[0].length() <= N){
			answer += msgs[0];
			curSize += msgs[0].length();
		}

        for(int i=1;i<msgs.length;i++){
            if(curSize + 1 + msgs[i].length() <= N){
                answer += " " + msgs[i];
                curSize += msgs[i].length() + 1;
                i++;
            }
			else{
				break;
			}
        }

        return answer;
    }
}
