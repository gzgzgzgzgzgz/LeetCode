class Solution:
    def dfs(self, i, isConnected, visited):
        visited[i] = True
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                #这一步会让j这一行与i相对应的entry变成visited
                self.dfs(j,isConnected, visited)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = len(isConnected) * [False]
        result = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                result+=1
                self.dfs(i, isConnected, visited)
        return result
                
            