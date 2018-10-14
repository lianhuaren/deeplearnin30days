#coding=utf-8

# //==================================================================
# // 《剑指Offer——名企面试官精讲典型编程题》代码
# // 作者：何海涛
# //==================================================================
#
# // 面试题12：矩阵中的路径
# // 题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有
# // 字符的路径。路径可以从矩阵中任意一格开始，每一步可以在矩阵中向左、右、
# // 上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入
# // 该格子。例如在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字
# // 母用下划线标出）。但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个
# // 字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
# // A B T G
# // C F C S
# // J D E H

class Solution:

    def hasPath(self, matrix, rows, cols, path):
        if matrix == None or rows < 1 or cols < 1 or path == None:
            return False
        visited = [0] * (rows * cols)

        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                print ("row:",row,"col:",col,"pathLength:",pathLength)
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLength, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, visited):
        if len(path) == pathLength:
            return True

        print ("--------------", "row:",row,"col:",col,"pathLength:",pathLength)

        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols \
            and matrix[row * cols + col] == path[pathLength] \
            and not visited[row * cols + col]:

            pathLength += 1
            visited[row * cols + col] = True

            hasPath = self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathLength, visited)

            print ("++++++++++++++++")
            if not hasPath:
                print ("***************")
                pathLength -= 1
                visited[row * cols + col] = False

        return hasPath


def main():



    s = Solution()

    print (s.hasPath("ABTGCFCSJDEH", 3, 4, "BFCE"))


if __name__ == '__main__':
    main()