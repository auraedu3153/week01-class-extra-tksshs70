def snail_board(row: int, col: int, clockwise=True) -> list[list[int]]:
    """
    행 개수 (row)와 열 개수 (col)을 받아 달팽이 배열을 만드는 함수.
    시작 위치는 (0, 0)이고, 방향은 인자 clockwise에 따라 시계방향 또는 반시계방향으로 설정됨.
    """
    rows = [0]*col
    board = [rows*row]
    for i in range(0,col):
        board[0][i]=i+1
    for j in range(0,row]:
        board[j][col]=col+j+1
