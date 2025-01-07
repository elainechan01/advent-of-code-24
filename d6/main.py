"""
Author: Elaine Chan @elainechan01
Date: 12/7/24
Program: Advent of Code Day 5: Print Queue
"""
from gg import GuardGallivant

def main():
    f = open("d6/datasets/input.txt", "r")
    try:
        f_contents = f.read()
        f_contents_split = [[val for val in row] for row in f_contents.split("\n")]
        gg = GuardGallivant(f_contents_split)
        res = gg.get_moves()
        
        print("===Part 1===")
        print(res)
        # print("===Part 2===")
        # print(res2)
    finally:
        f.close()

if __name__ == "__main__":
    main()