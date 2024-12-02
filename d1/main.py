"""
Author: Elaine Chan @elainechan01
Date: 12/2/24
Program: Advent of Code Day 1 - Historian Hysteria
"""
from hh import HystorianHysteria

def main():
    f = open("d1/datasets/input.txt", "r")
    try:
        f_contents = f.read()
        f_contents_split = f_contents.split('\n')
        
        hh = HystorianHysteria()
        hh.getLists(f_contents_split)
        res = hh.calcSumOfDist()
        res2 = hh.calcSimilarityScore()
        
        print("===Part 1===")
        print(res)
        print("===Part 2===")
        print(res2)
    finally:
        f.close()

if __name__ == "__main__":
    main()