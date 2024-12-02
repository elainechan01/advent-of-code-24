"""
Author: Elaine Chan @elainechan01
Date: 12/2/24
Program: Advent of Code Day 1 - Historian Hysteria
"""
import bisect

class HystorianHysteria:
    def __init__(self) -> None:
        self.list1 = []
        self.list2 = []

    def getLists(self, locationIDs: list) -> None:
        for IDs in locationIDs:
            ID1, ID2 = IDs.split()
            bisect.insort(self.list1, ID1)
            bisect.insort(self.list2, ID2)
    
    def calculateSumOfDist(self) -> int:
        res = sum([abs(int(self.list1[i]) - int(self.list2[i])) for i in range(len(self.list1))])
        return res