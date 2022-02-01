class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        int idx = 0;
        int flag = 0;
        
        char[] skills = skill.toCharArray();
        
        for(String s : skill_trees){
            idx = 0;
            flag = 0;
            for(int i=0;i<s.length();i++){
                for(int j=idx;j<skills.length;j++){
                    if(s.charAt(i) == skills[j]){
                        if(idx == j){
                            idx++;
                            break;
                        }
                        else{
                            flag = 1;
                            break;
                        }
                    }
                }
            }
            if(flag == 0){
                answer++;
            }
        }
        
        return answer;
    }
}