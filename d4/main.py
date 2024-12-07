"""
Author: Elaine Chan @elainechan01
Date: 12/6/24
Program: Advent of Code Day 4: Ceres Search
"""
from cs import CeresSearch

def main():
    f = open("d4/datasets/input.txt", "r")
    try:
        f_contents = f.read()
        f_contents_split = f_contents.split('\n')
        cs = CeresSearch([[val for val in line] for line in f_contents_split])
        res = cs.count_xmas()
        
        print("===Part 1===")
        print(res)
        # print("===Part 2===")
        # print(res2)
    finally:
        f.close()

if __name__ == "__main__":
    main()