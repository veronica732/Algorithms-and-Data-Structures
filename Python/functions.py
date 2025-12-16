#Day 1
def twoSum(nums, target):
    """
    Find indices of two numbers that sum to target.
    
    Inputs:
        nums: List[int] - array of integers
        target: int - target sum
        
    Output:
        List[int] - two indices or empty list if no solution
    """
    H = {}  
    
    for i in range(len(nums)):  
        complement = target - nums[i] 
        
        if complement in H:  
            return [H[complement], i]  
        else:
            H[nums[i]] = i  
    
    return []  


# Day 2

def max_sub_array(nums):

    """
    Finds the contiguous subarray (containing at least one number) which 
    has the largest sum and returns its sum.
    
    This implementation uses Kadane's Algorithm, which operates in linear time.
    
    Args:
        nums (List[int]): A list of integers.
        
    Returns:
        int: The maximum subarray sum. If the input list is empty, returns 0.
        
    """
    
    if not nums:
        return 0

    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        
        max_sum = max(max_sum, current_sum)

    return max_sum

# DAY 3 
def sortColors(nums):
    """
    Sorts an array of objects colored red, white, and blue in-place.
    The integers 0, 1, and 2 represent red, white, and blue respectively.
    
    This uses the Dutch National Flag algorithm with three pointers:
    - low: boundary for 0s
    - mid: current element being scanned
    - high: boundary for 2s

    Args:
        nums (List[int]): List of integers containing only 0, 1, and 2.
        
    Returns:
        None: The list is modified in-place.
    """
   
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


## Day 17
def spiralorder(mat):
    """
    Input : m x n matrix
    
    Return a list (M) of all entries of the matrix in spiral order(clockwise) starting from mat[0,0]
    
    """
    
    M = []
    top = 0                     
    bottom = len(mat) - 1       
    left = 0                     
    right = len(mat[0]) - 1
    
    while top<= bottom and left<=right:
        
        for col in range(left, right + 1):
            M.append(mat[top][col])
        top += 1
        
        for row in range(top + 1, bottom):
            M.append(mat[row][right])
        right -= 1
        
        if top <= bottom:
            for col in range(right, left - 1, -1):
                M.append(mat[bottom][col])
            bottom -= 1
            
        if left <= right:
            for row in range(bottom, top - 1, -1):
                M.append(mat[row][left])
            left += 1
            
    return M
        

# DAY 18: VALID SUDOKU
def isValidSudoku(board):
    """
    Check if Sudoku board is valid.
    
    Inputs:
        board: List[List[str]] - 9x9 Sudoku board
        
    Output:
        bool - True if valid, False otherwise
    """
    
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == '.':
                continue
            
            
            if num in rows[r]:
                return False
            rows[r].add(num)
            
            
            if num in cols[c]:
                return False
            cols[c].add(num)
            
            
            box_idx = (r // 3) * 3 + (c // 3)
            if num in boxes[box_idx]:
                return False
            boxes[box_idx].add(num)
    
    return True
    


# DAY 19: WORD SEARCH
def exist(board, word):
    """
    Check if word exists in grid.
    
    Inputs:
        board: List[List[str]] - m x n character grid
        word: str - word to search
        
    Output:
        bool - True if word exists
    """
    m, n = len(board), len(board[0])
    
    def dfs(r, c, index):
        
        if index == len(word):
            return True
        
        
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
            return False
        
        
        temp = board[r][c]
        board[r][c] = '#'
        
    
        found = (dfs(r+1, c, index+1) or
                 dfs(r-1, c, index+1) or
                 dfs(r, c+1, index+1) or
                 dfs(r, c-1, index+1))
        
        
        board[r][c] = temp
        return found
    
    
    for r in range(m):
        for c in range(n):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True
    
    return False


