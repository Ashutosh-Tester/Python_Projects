def nQueens(n):
    res = []

    def isSafe(mat, row, col):
        for i in range(row):
            if mat[i][col] == 1:
                return False
        i, j = row, col
        while i>=0 and j >= 0:
            if mat[i][j] == 1:
                return False
            i = i-1
            j = j-1       
        i, j = row, col
        while i>=0 and j<len(mat):
            if mat[i][j] == 1:
                return False
            i = i-1
            j = j+1
        return True
    def addSolution(chessboard):
        currans = []
        for i in chessboard:
            currans.extend(i)
        res.append(currans)
       def SolveNQueens(mat, row):
        if row == len(mat):
            addSolution(mat)
            return

        for i in range(len(mat)):
            if isSafe(mat, row, i):
                mat[row][i] = 1

                SolveNQueens(mat, row+1)

                mat[row][i] = 0
    
    
    mat = [[0 for _ in range(n)] for _ in range(n)]
    SolveNQueens(mat, 0)
    return res

n = 4
res = nQueens(n)
print(res)
