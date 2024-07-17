class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Brute Force Method

        # value = float(inf)
        # m = len(matrix) #rows
        # n = len(matrix[0]) #columns
        # # Brute force method
        # def setColumn(j):
        #     for i in range(m):
        #         if matrix[i][j]!=0:
        #             matrix[i][j]= value
        # def setRow(i):
        #     for j in range(n):
        #         if matrix[i][j]!=0:
        #             matrix[i][j] = value

        # def zeroMatrix():
        #     for i in range(m):
        #         for j in range(n):
        #             if(matrix[i][j]==0):
        #                 setColumn(j)
        #                 setRow(i)
        #     for i in range(m):
        #         for j in range(n):
        #             if matrix[i][j] == value:
        #                 matrix[i][j] = 0
        # zeroMatrix()
        
        # Better Solution : as we are not changing the elements to zero at the traversal itself, but only at the end of the traversal

        # m = len(matrix)
        # n = len(matrix[0])

        # row = [0]*m
        # column = [0]*n

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j]==0:
        #             row[i] = -1
        #             column[j] = -1

        # for i in range(m):
        #     for j in range(n):
        #         if (row[i] == -1 or column[j] == -1):
        #             matrix[i][j] = 0

        # Optimal solution

        m = len(matrix) #row
        n = len(matrix[0]) #column
        
        col0 = 1
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[i][0]=0

                    if j!=0:
                        matrix[0][j]=0
                    else:
                        col0 = 0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j]=0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(m):
                matrix[i][0] = 0

