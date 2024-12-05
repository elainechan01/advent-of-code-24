"""
Author: Elaine Chan @elainechan01
Date: 12/4/24
Program: Advent of Code Day 2: Red-Nosed Reports
"""
import bisect
from collections import Counter

class RedNosedReports:
    def __init__(self) -> None:
        pass

    def checkReports(self, reports: list) -> int:
        '''
        Returns the number of safe reports
        '''
        res = 0
        for report in reports:
            safe = True
            prev = report.pop(0)
            next = report.pop(0)
            if next > prev and next - prev <= 3:
                is_increase = True
                prev = next
            elif next < prev and prev - next <= 3:
                is_increase = False
                prev = next
            else:
                continue
            while report:
                next = report.pop(0)
                if (next > prev and is_increase and next - prev <= 3) or (next < prev and not is_increase and prev - next <= 3):
                    prev = next
                else:
                    safe = False
                    break
            if not report and safe:
                res += 1
        return res
