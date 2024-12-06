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
        self.mul_instructions = []

    def getMultiplicationsOnly(self, text: str) -> None:
        '''
        Retrieves all matches of multiplication e.g., 'mul(2,3)'

        Pattern:
        () Capturing group - all characters matched within these parantheses will be extracted and returned
        '''
        pattern = r"mul\((\d+),(\d+)\)" 
        matches = re.findall(pattern, text)
        for match in matches:
            try:
                self.mul.append(list(map(int, match)))
            except ValueError:
                pass
    
    def calculateSumOfMultiplications(self) -> int:
        return sum([functools.reduce(lambda a, b: a * b, pair) for pair in self.mul])

    def getConditionalMultiplications(self, text: str) -> None:
        '''
        Retrieves all matches of multiplication e.g., 'mul(2,3)' and conditional instructions e.g., do(), don't()
        '''
        pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
        matches = re.findall(pattern, text)
        
        for match in matches:
            try:
                self.mul_instructions.append(list(map(int, filter(None,match))))
            except ValueError:
                self.mul_instructions.append(list(filter(None,match))[0])
        print(self.mul_instructions)
    
    def calculateSumOfMultiplicationWithConditions(self) -> int:
        go = True
        res = 0
        for val in self.mul_instructions:
            if val == "do()":
                go = True
            elif val == "don't()":
                go = False
            else:
                if go:
                    res += val[0] * val[1]
        return res
