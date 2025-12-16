from functions import spiralorder
from functions import isValidSudoku
from functions import exist
from functions import twoSum
from functions import max_sub_array


# Day 1

nums1 = [2, 7, 11, 15]
target1 = 17
print(twoSum(nums1, target1))

# Day 2
test_input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Maximum Subarray Sum: {max_sub_array(test_input)}")

# Day 17
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
    [21, 22, 23, 24]
]

print(spiralorder(matrix))

# Day 18
sudoku_board = [
    [5, 3, ".", ".", 7, ".", ".", ".", "."],
    [6, ".", ".", 1, 9, 5, ".", ".", "."],
    [".", 9, 8, ".", ".", ".", ".", 6, "."],
    [8, ".", ".", ".", 6, ".", ".", ".", 3],
    [4, ".", ".", 8, ".", 3, ".", ".", 1],
    [7, ".", ".", ".", 2, ".", ".", ".", 6],
    [".", 6, ".", ".", ".", ".", 2, 8, "."],
    [".", ".", ".", 4, 1, 9, ".", ".", 5],
    [".", ".", ".", ".", 8, ".", ".", 7, 9]
]

if isValidSudoku(sudoku_board):
    print("The Sudoku board is valid!")
else:
    print("Invalid Sudoku board.")

# Day 19

grid = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]

print(exist(grid, "ABCCED")) 
print(exist(grid, "SEE"))    
print(exist(grid, "ABCB")) 

print(exist(grid, "ABFA"))