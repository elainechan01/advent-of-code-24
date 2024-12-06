"""
Author: Elaine Chan @elainechan01
Date: 12/5/24
Program: Advent of Code Day 3: Mull It Over
"""
import re
import functools

class MullItOver:
    def __init__(self) -> None:
        self.mul = []

    def getMultiplicationsOnly(self, text: str) -> None:
        '''
        Retrieves all matches of multiplication e.g., 'mul(2,3)'

        Pattern:
        () Capturing group - all characters matched within these parantheses will be extracted and returned
        '''
        print("Start", text)
        pattern = r"mul\((\d+),(\d+)\)" 
        matches = re.findall(pattern, text)
        print(matches)
        for match in matches:
            try:
                self.mul.append(list(map(int, match)))
            except ValueError:
                pass
    
    def calculateSumOfMultiplications(self) -> int:
        return sum([functools.reduce(lambda a, b: a * b, pair) for pair in self.mul])
