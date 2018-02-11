class Collatz:
    def __init__(self):
        self.cache = {}

    def chainLength(self, start_number):
        """Returns the length of a Collatz chain starting at start_number."""
        
        number = start_number
        number_of_steps = 1
        while number != 1:
            if number in self.cache:
                new_steps = number_of_steps + self.cache[number]
                self.cache[start_number] = new_steps
                return
            elif number % 2 == 0:
                number /= 2
            else:
                number = 3 * number + 1
            number_of_steps += 1
        self.cache[start_number] = number_of_steps
        return

    def largestChain(self, number):
        """Returns the largest Collatz chain where first term is < number."""

        for i in range(1, number):
            self.chainLength(i)
        sorted_values = sorted(self.cache, key=self.cache.get, reverse=True)
        return (sorted_values[0])

if __name__ == "__main__":
    collatz = Collatz()
    print(collatz.largestChain(1000000))
