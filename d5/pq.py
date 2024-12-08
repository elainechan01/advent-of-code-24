"""
Author: Elaine Chan @elainechan01
Date: 12/7/24
Program: Advent of Code Day 5: Print Queue
"""
from collections import defaultdict

class PrintQueue:
    def __init__(self, rules: list, updates: list) -> None:
        self.rules = rules
        self.updates = updates
        self.order = defaultdict(list)
        self.valid_updates = []
        self.invalid_updates = []
        self.__get_order()
        self.__get_valid_updates()
    
    def __get_order(self) -> None:
        '''
        Parse rules to determine expected page orders
        '''
        for rule in self.rules:
            self.order[rule[0]].append(rule[1])
    
    def __get_valid_updates(self) -> None:
        '''
        Filter out the valid orders (adheres to rules)
        '''
        for update in self.updates:
            valid = True
            # print("Start", update[:-1])
            for idx, page in enumerate(update[:-1]):
                # print(page, idx)
                # print("postfix", update[idx+1:], [val in self.order[page] for val in update[idx+1:]])
                # print("prefix", [page in self.order[val] for val in update[:idx]])
                if not all([val in self.order[page] for val in update[idx+1:]] + [page in self.order[val] for val in update[:idx]]):
                    valid = False
                    break
            if valid:
                self.valid_updates.append(update)
            else:
                self.invalid_updates.append(update)
        # print(self.valid_updates)
    
    def calculate_middle_of_valid_updates(self) -> int:
        '''
        Calculate the sum of the middle page number of correctly-ordered updates
        '''
        res = sum([valid[len(valid)//2] for valid in self.valid_updates])
        return res

    def calculate_middle_of_invalid_updates(self) -> int:
        '''
        Calculate the sum of the middle page number of incorrectly-ordered updates after they've been reordered correctly
        '''
        res = 0
        for invalid in self.invalid_updates:
            length = len(invalid)
            valid = [0] * length
            for idx, page in enumerate(invalid):
                pages_after = len(list(filter(lambda val: val in self.order[page], invalid[:idx] + invalid[idx+1:])))
                valid[length - pages_after - 1] = page
            res += valid[length//2]
        return res