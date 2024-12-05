"""
Author: Elaine Chan @elainechan01
Date: 12/2/24
Program: Advent of Code Day 2: Red-Nosed Reports
"""
from rnr import RedNosedReports

def main():
    f = open("d2/datasets/input.txt", "r")
    try:
        f_contents = f.read()
        f_contents_split = f_contents.split('\n')
        f_contents_split = [[int(num) for num in report.split()] for report in f_contents_split]
        
        rnr = RedNosedReports()
        res = rnr.checkReports(f_contents_split)
        
        print("===Part 1===")
        print(res)
        # print("===Part 2===")
        # print(res2)
    finally:
        f.close()

if __name__ == "__main__":
    main()