from sequentials.sequential import *


class SequentialSearch(Sequential):

    def __init__(self):
        self.counts = []

    def __search__(self, numbers, number):
        pos = 0
        count = 0
        found = False

        while pos < len(numbers) and found is False:
            if numbers[pos] == number:
                found = True
            else:
                pos = pos + 1
            count += 1
        self.counts.append(count)
        return found
