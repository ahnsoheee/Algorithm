import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> h = new HashMap<>();
    	
    	for(int i = 0; i < clothes.length; i++) {
    		if(h.get(clothes[i][1]) == null)
    			h.put(clothes[i][1], 1);
    		else
    			h.put(clothes[i][1], h.get(clothes[i][1]) + 1);
    	}
    	
    	for(String keys: h.keySet()) {
    		answer *= (h.get(keys) + 1);
    	}
        
    	answer -= 1;
        return answer;
    }
}