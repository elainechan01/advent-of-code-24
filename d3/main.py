"""
Author: Elaine Chan @elainechan01
Date: 12/2/24
Program: Advent of Code Day 2: Red-Nosed Reports
"""
from mio import MullItOver

def main():
    f = open("d3/datasets/input.txt", "r")
    try:
        f_contents = f.read()
        mio = MullItOver()
        mio.getMultiplicationsOnly(f_contents)
        res = mio.calculateSumOfMultiplications()
        
        print("===Part 1===")
        print(res)
        print("===Part 2===")
        # print(res2)
    finally:
        f.close()

if __name__ == "__main__":
    main()