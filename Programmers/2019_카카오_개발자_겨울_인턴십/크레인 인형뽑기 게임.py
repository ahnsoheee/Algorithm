def solution(board, moves):
    answer = 0
    basket = []
    cnt = -1
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                basket.append(board[i][move-1])
                board[i][move-1] = 0
                cnt += 1
                if cnt >= 1 and basket[cnt] == basket[cnt-1]:
                    basket = basket[:-2]
                    cnt -= 2
                    answer += 2
                break
                
    return answer