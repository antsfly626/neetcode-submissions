from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[] for i in range(9)]
        blocks = defaultdict(set)
        for row_num, row in enumerate(board):
            x = [i for i in row if i!='.']
            if len(set(x))<len(x):
                return False
            for col_num, item in enumerate(row):
                cols[col_num].append(item)
                if item != '.':
                    box_key = (row_num // 3, col_num // 3)
                    if item in blocks[box_key]:
                        return False
                    blocks[box_key].add(item)


        for col in cols:
            x = [i for i in col if i!='.']
            if len(set(x))<len(x):
                return False
        return True
        