def checkmate(board):
    try:
        rows = board.strip().split('\n')
        if not rows:
            return
        
        n = len(rows)
        for row in rows:
            if len(row) != n:
                return
                
    except:
        return

    king_pos = None
    for r in range(n):
        for c in range(n):
            if rows[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break
            
    if not king_pos:
        print("Fail")
        return

    kr, kc = king_pos

    def is_valid(r, c):
        return 0 <= r < n and 0 <= c < n

    pawn_attacks = [
        (kr + 1, kc - 1),
        (kr + 1, kc + 1)
    ]
    for pr, pc in pawn_attacks:
        if is_valid(pr, pc) and rows[pr][pc] == 'P':
            print("Success")
            return

    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    straights = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in diagonals:
        r, c = kr + dr, kc + dc
        while is_valid(r, c):
            piece = rows[r][c]
            if piece == 'B' or piece == 'Q':
                print("Success")
                return
            if piece in ['P', 'R']:
                break
            r += dr
            c += dc

    for dr, dc in straights:
        r, c = kr + dr, kc + dc
        while is_valid(r, c):
            piece = rows[r][c]
            if piece == 'R' or piece == 'Q':
                print("Success")
                return
            if piece in ['P', 'B']:
                break
            r += dr
            c += dc

    print("Fail")
