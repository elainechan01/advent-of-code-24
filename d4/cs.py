"""
Author: Elaine Chan @elainechan01
Date: 12/6/24
Program: Advent of Code Day 4: Ceres Search
"""
import re
import numpy as np

class CeresSearch:
    def __init__(self, ws: list) -> None:
        self.ws = ws
        # print(self.ws)
    
    def count_xmas(self) -> int:
        '''
        Count the number of times XMAS appears horizontally, vertically, diagonally, and written backwards
        '''
        res = 0
        all_horizontal = self.ws + [line[::-1] for line in self.ws]
        all_vertical = [[self.ws[row][col] for row in range(len(self.ws))] for col in range(len(self.ws[0]))]
        all_vertical += [line[::-1] for line in all_vertical]
        all_diagonal = []
        for k in range(-(len(self.ws) - 1), len(self.ws[0])):   # lr diagonal
            all_diagonal.append(np.diagonal(self.ws, offset=k))
            all_diagonal.append(np.diagonal(self.ws, offset=k)[::-1])
        for k in range(len(self.ws) - 1, -len(self.ws[0]), -1):     # rl diagonal
            all_diagonal.append(np.diagonal(np.fliplr(self.ws), offset=k))
            all_diagonal.append(np.diagonal(np.fliplr(self.ws), offset=k)[::-1])
        all = all_horizontal + all_vertical + all_diagonal
        # get number of occurrences
        for text in all:
            # print("Start", "".join(text))
            # print(res, re.findall("XMAS", "".join(text)))
            res += len(re.findall("XMAS", "".join(text)))
        return res
    
    def count_x_mas(self) -> int:
        '''
        Count the number of times X-MAS appears
        '''
        res = 0
        rows = len(self.ws)
        cols = len(self.ws[0])
        for row in range(rows):
            for col in range(cols):
                if 0 <= row-1 and 0 <= col-1 and row+1 < rows and col+1 < cols: 
                    lr = self.ws[row-1][col-1] + self.ws[row][col] + self.ws[row+1][col+1]
                    rl = self.ws[row-1][col+1] + self.ws[row][col] + self.ws[row+1][col-1]
                    if (lr == "MAS" or lr == "SAM") and (rl == "MAS" or rl == "SAM"):
                        res += 1
        return res
