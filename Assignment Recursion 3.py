#Q3. Finding the length of connected cells of 1’ s (regions) in an matrix of 0s and 1’s.


def Safe(m, row, col, visited): #function to check if a given row,col can be included in DFS
    return ((row >= 0) and (row < row1) and(col >= 0) and (col < col1) and (m[row][col] and not visited[row][col]))   

def DFS(m, row, col, visited, count): #function to do DFS for a 2D boolean matrix. It only considers the 8 neighbours as adjacent vertices 
    rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]  
    colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
    visited[row][col] = True

    for k in range(8): 
        if (Safe(m, row + rowNbr[k],col + colNbr[k], visited)): 
            count[0] += 1
            DFS(m, row + rowNbr[k], col + colNbr[k], visited, count) 
  
def largestRegion(M): #this is the main function that returns the largest region in the given 2d matrix
    visited = [[0] * col1 for i in range(row1)] 
    result = -999999999999
    for i in range(row1): 
        for j in range(col1): 
            if (M[i][j] and not visited[i][j]): 
                count = [1]  
                DFS(M, i, j, visited , count)  
                result = max(result , count[0]) 
    return result

row1 = 5
col1 = 5
M = [[1,1,0,0,0], 
     [0,1,1,0,0],  
     [0,0,1,0,1], 
     [1,0,0,0,1],
     [0,1,0,1,1]]

print(largestRegion(M)) 
