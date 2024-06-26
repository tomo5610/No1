def count_stones(S):
    board = ['B', 'W']
    
    # 現在の手番
    turn = 1  # 1が黒(B)、-1が白(W)
    
    # 指定された位置に石を置き、間の石をひっくり返す関数
    def place_stone(position, color):
        nonlocal board
        
        if position == 'L':
            board.insert(0, color)
        else:
            board.append(color)
        
        # ひっくり返し処理
        flip_stones(color)
    
    # ひっくり返し処理の関数
    def flip_stones(new_color):
        nonlocal board
        
        left_idx = None
        right_idx = None
        
        for i in range(len(board)):
            if board[i] == new_color:
                if left_idx is None:
                    left_idx = i
                right_idx = i
        
        # 挟まれている石をひっくり返す
        if left_idx is not None and right_idx is not None:
            for i in range(left_idx + 1, right_idx):
                board[i] = new_color
    
    # 棋譜に従って石を置く
    for move in S:
        if turn == 1:
            place_stone(move, 'B')
        else:
            place_stone(move, 'W')
        turn *= -1
    
    black_count = board.count('B')
    white_count = board.count('W')
    
    return black_count, white_count

if __name__ == "__main__":
    S = input().strip()
    black, white = count_stones(S)
    print(black, white)
