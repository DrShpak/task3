class Sequential:
    counts = []

    def sum(self):
        sum = 0
        for count in self.counts:
            sum += count
        return sum

    def __search__(self, numbers, number):
        pass

    def write_number_of_comparisons(self, path):
        output = open(path, "w")
        output.write(str(self.sum() / len(self.counts)))
        output.close()
