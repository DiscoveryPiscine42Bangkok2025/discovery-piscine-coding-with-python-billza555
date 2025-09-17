def checkmate(board: str):
    rows = board.strip().split("\n")
    size = len(rows)
    grid = [list(r) for r in rows]

    king_pos = None
    for y in range(size):
        for x in range(len(grid[y])):
            if grid[y][x] == "K":
                king_pos = (y, x)
                break
    if king_pos is None:
        print("Error")
        return
    
    def inside(y, x):
        return 0 <= y < size and 0 <= x < len(grid[y])
    
    ky, kx = king_pos
    
    for dy, dx in [(1, -1), (1, 1)]:
        y, x = ky + dy, kx + dx
        if inside(y, x) and grid[y][x] == "P":
            print("Success")
            return

    for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        y, x = ky, kx
        while True:
            y += dy
            x += dx
            if not inside(y, x):
                break
            if grid[y][x] != ".":
                if grid[y][x] in ["B", "Q"]:
                    print("Success")
                    return
                break

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        y, x = ky, kx
        while True:
            y += dy
            x += dx
            if not inside(y, x):
                break
            if grid[y][x] != ".":
                if grid[y][x] in ["R", "Q"]:
                    print("Success")
                    return
                break

    print("Fail")