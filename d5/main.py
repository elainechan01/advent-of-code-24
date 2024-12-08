"""
Author: Elaine Chan @elainechan01
Date: 12/7/24
Program: Advent of Code Day 5: Print Queue
"""
from pq import PrintQueue

def main():
    f = open("d5/datasets/input.txt", "r")
    try:
        f_contents = f.read()
        f_contents_split = f_contents.split('\n\n')
        rules = [list(map(int, pair.split("|"))) for pair in f_contents_split[0].split('\n')]
        updates = [list(map(int, update.split(","))) for update in f_contents_split[1].split('\n')]
        pq = PrintQueue(rules, updates)
        res = pq.calculate_middle_of_valid_updates()
        res2 = pq.calculate_middle_of_invalid_updates()
        
        print("===Part 1===")
        print(res)
        print("===Part 2===")
        print(res2)
    finally:
        f.close()

if __name__ == "__main__":
    main()