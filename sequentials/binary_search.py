from sequentials.sequential import *


class BinarySearch(Sequential):

    def __init__(self):
        self.counts = []

    def __search__(self, numbers, number):
        numbers = sorted(numbers)
        low_bound = 0
        high_bound = len(numbers) - 1
        count = 0

        while low_bound <= high_bound:
            count += 1
            mid = (low_bound + high_bound) // 2
            if number < numbers[mid]:
                high_bound = mid - 1
            elif number > numbers[mid]:
                low_bound = mid + 1
            else:
                self.counts.append(count)
                return True
        self.counts.append(count)
        return False
