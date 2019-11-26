from sequentials.sequential import Sequential


class InterpolationSearch(Sequential):

    def __init__(self):
        self.counts = []

    # вернёт индекс со значением элемента number или -1 в случае, если такого элемента в массиве нет
    def __search__(self, numbers, key):
        numbers = sorted(numbers)
        left = 0
        right = len(numbers) - 1
        count = 0

        while numbers[left] < key < numbers[right]:
            mid = left + (key - numbers[left]) * (right - left) // (numbers[right] - numbers[left])
            count += 1
            if numbers[mid] < key:
                left = mid + 1
            elif numbers[mid] > key:
                right = mid - 1
            else:
                self.counts.append(count)
                return mid

        if numbers[left] == key:
            count += 1
            self.counts.append(count)
            return left
        elif numbers[right] == key:
            count += 1
            self.counts.append(count)
            return right
        else:
            return -1
