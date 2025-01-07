"""
Author: Elaine Chan @elainechan01
Date: 12/7/24
Program: Advent of Code Day 5: Print Queue
"""
from collections import defaultdict

class GuardGallivant:
    def __init__(self, map: list) -> None:
        self.map = map
        self.__ori_pos = None
        self.__get_start_pos()

    def __get_start_pos(self) -> None:
        for row_idx, row in enumerate(self.map):
            if "^" in row:
                col_idx = row.index("^")
                self.__ori_pos = (row_idx, col_idx)
                break
    
    def get_moves(self) -> int:
        curr = self.__ori_pos
        visited = [curr]
        # print("start", curr)
        dir = "up"
        while 0 <= curr[0] < len(self.map) and 0 <= curr[1] < len(self.map[0]):

            if dir == "up":
                next = (curr[0] - 1, curr[1])
            elif dir == "down":
                next = (curr[0] + 1, curr[1])
            elif dir == "left":
                next = (curr[0], curr[1] - 1)
            else:
                next = (curr[0], curr[1] + 1)

            if 0 <= next[0] < len(self.map) and 0 <= next[1] < len(self.map[0]):
                if self.map[next[0]][next[1]] == "#":
                    # print("switching direction from", dir)
                    if dir == "up":
                        dir = "right"
                    elif dir == "down":
                        dir = "left"
                    elif dir == "left":
                        dir = "up"
                    elif dir == "right":
                        dir = "down"
                else:
                    # print("moving", next, "|| visited?", next in visited, "|| TOTAL BEFORE CHECKING:", len(visited))
                    if next not in visited:
                        visited.append(next)
                    curr = next
            else:
                break
        return len(visited)
        
                