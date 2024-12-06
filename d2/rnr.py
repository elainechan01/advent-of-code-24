"""
Author: Elaine Chan @elainechan01
Date: 12/4/24
Program: Advent of Code Day 2: Red-Nosed Reports
"""
from copy import deepcopy

class RedNosedReports:
    def __init__(self) -> None:
        pass

    def checkReports(self, reports: list) -> int:
        '''
        Returns the number of safe reports
        '''
        res = 0
        reports_clone = deepcopy(reports)
        for report in reports_clone:
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

    def checkReportsWithProblemDampener(self, reports: list) -> int:
        '''
        Returns the number of safe reports using the Problem Dampener
        '''
        increasing_limit = {1, 2, 3}
        decreasing_limit = {-1, -2, -3}
        res = 0
        for report in reports:
            level = [report[i+1] - report[i] for i in range(len(report)-1)]
            if all([val in increasing_limit for val in level]) or all([val in decreasing_limit for val in level]):
                res += 1
            else:
                for i in range(len(report)):
                    lvl_removed_report = report[:i] + report[i+1:]
                    level = set([lvl_removed_report[i+1] - lvl_removed_report[i] for i in range(len(lvl_removed_report)-1)])
                    if level <= increasing_limit or level <= decreasing_limit:
                        res += 1
                        break
        return res
