def solution(s):
    answer = 1001
    
    if len(s) == 1:
        return 1
    
    for size in range(1, len(s)//2 + 1):
        compression = ''    
        piece = s[:size]
        cnt = 1
        
        for i in range(size, len(s), size):
            if piece == s[i:i+size]:
                cnt += 1
            else:
                if cnt != 1:
                    compression += str(cnt) + piece
                else:
                    compression += piece
                    
                cnt = 1
                piece = s[i:i+size]
                
        if cnt != 1:
            compression += str(cnt) + piece
        else:
            compression += piece
            
        answer = min(answer, len(compression))
        
    return answer