class Solution {
    public String solution(String m, String[] musicinfos) {
        String answer = "";
        int max = 0;
            
        for (String musicinfo: musicinfos) {
            String[] info = musicinfo.split(",");
        
            String[] start = info[0].split(":");
            String[] end = info[1].split(":");
            int time = (Integer.parseInt(end[0]) - Integer.parseInt(start[0])) * 60 + Integer.parseInt(end[1]) - Integer.parseInt(start[1]);
            
            String replaced_code = replace_code(info[3]);
            String code = "";
            
            for (int i = 0; i < time / replaced_code.length(); i++)
                code += replaced_code;
            
            code += replaced_code.substring(0, time % replaced_code.length());
            
            if (code.contains(replace_code(m))) {
                if (max < time) {
                    max = time;
                    answer = info[2];
                }
            }
        }
        
        if (answer == "")
            answer = "(None)";
        
        return answer;
    }
    
    public String replace_code(String code) {
        code = code.replaceAll("C#", "c");
        code = code.replaceAll("D#", "d");
        code = code.replaceAll("F#", "f");
        code = code.replaceAll("G#", "g");
        code = code.replaceAll("A#", "a");

        return code;
    }
}