class Solution {
    boolean solution(String s) {

        int p = s.replaceAll("[^pP]", "").length();
        int y = s.replaceAll("[^yY]", "").length();
        
        return (p==y) ? true : false;

    }
}