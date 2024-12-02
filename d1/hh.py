"""
Author: Elaine Chan @elainechan01
Date: 12/2/24
Program: Advent of Code Day 1 - Historian Hysteria
"""
import bisect
from collections import Counter

class HystorianHysteria:
    def __init__(self) -> None:
        self.list1 = []
        self.list2 = []

    def getLists(self, locationIDs: list) -> None:
        for IDs in locationIDs:
            ID1, ID2 = IDs.split()
            bisect.insort(self.list1, ID1)
            bisect.insort(self.list2, ID2)
    
    def calcSumOfDist(self) -> int:
        res = sum([abs(int(self.list1[i]) - int(self.list2[i])) for i in range(len(self.list1))])
        return res
    
    def calcSimilarityScore(self) -> int:
        list2_frequency = Counter(self.list2)
        res = sum([int(num) * list2_frequency[num] for num in self.list1])
        return res