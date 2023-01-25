def solution(board, aloc, bloc):
    R, C = len(board), len(board[0])
    
    def get_next_positions(pos):
        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
        r, c = pos[0], pos[1]
        positions = []

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 1:
                positions.append([nr, nc])
        
        return positions
    
    def solve(aloc, bloc, turn):
        player = turn % 2 == 0
        ar, ac, br, bc = aloc[0], aloc[1], bloc[0], bloc[1]
        next_positions = get_next_positions(aloc if player else bloc)
        
        if not next_positions: 
            return not player, turn
        
        if aloc == bloc: 
            return player, turn + 1
    
        win_moves, lose_moves = [], []
    
        if player:
            board[ar][ac] = 0
            for nr, nc in next_positions:
                winner, moves = solve([nr, nc], bloc, turn + 1)
                if player == winner: 
                    win_moves.append(moves)
                else: 
                    lose_moves.append(moves)
            board[ar][ac] = 1
        else:
            board[br][bc] = 0
            for nr, nc in next_positions:
                winner, moves = solve(aloc, [nr, nc], turn + 1)
                if player == winner: 
                    win_moves.append(moves)
                else: 
                    lose_moves.append(moves)
            board[br][bc] = 1
        
        if win_moves:
            return player, min(win_moves)
        else:
            return not player, max(lose_moves)
    
    _, answer = solve(aloc, bloc, 0)
    
    return answer
