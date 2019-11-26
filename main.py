from sequentials.binary_search import BinarySearch
from sequentials.sequential_search import SequentialSearch
from sequentials.interpolation_search import InterpolationSearch


def read():
    file = open("input.txt", 'r')
    return file


def get_numbers(file):
    string_numbers = str(file.readline()).split()
    numbers = []
    i = 0
    for num in string_numbers:
        numbers.append(int(num))
        i += 1
    return numbers


def search(numbers, sequential, path):
    for i in range(0, len(numbers)):
        sequential.__search__(numbers, numbers[i])
    sequential.write_number_of_comparisons(path)


# последовательный поиск
sequential_search_obj = SequentialSearch()
search(get_numbers(read()), sequential_search_obj, "output/output1.txt")

# бинарный поиск
binary_search_obj = BinarySearch()
search(get_numbers(read()), binary_search_obj, "output/output2.txt")

# интеполяционный поиск
interpolation_search_obj = InterpolationSearch()
search(get_numbers(read()), interpolation_search_obj, "output/output3.txt")