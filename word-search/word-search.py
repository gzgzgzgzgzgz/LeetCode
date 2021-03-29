class Solution:
    def dfs(self, board, i, j, visited, k, word):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[k] :
            return False 
        if k == len(word) - 1: return True
        #visited[i][j] = True
        board[i][j] = ''
        res = self.dfs(board, i-1,j,visited, k + 1, word) or self.dfs(board, i+1,j,visited, k + 1, word) or self.dfs(board, i,j - 1,visited, k + 1, word) or self.dfs(board, i,j + 1,visited, k + 1, word)
        #visited[i][j] = False
        board[i][j] = word[k]
        return res
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False] * len(board[0])] * len(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j,  visited, 0, word):
                    return True
        return False
        