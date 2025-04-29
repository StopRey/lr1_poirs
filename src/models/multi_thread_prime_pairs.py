from sympy import isprime
from multiprocessing import Pool

class MultiThreadPrimePairs:
    def __init__(self, num_processes: int = 4):
        self.num_processes = num_processes

    def _count_pairs(self, args):
        start, end, prev_prime = args
        count = 0
        last_prime = prev_prime
        i = start
        while i < end:
            if isprime(i):
                if last_prime is not None and i - last_prime == 2:
                    count += 1
                last_prime = i
                i += 2
            else:
                i += 2
        return count, last_prime

    def calculate(self, n: int) -> int:
        step = (n - 3) // self.num_processes + 1
        ranges = []
        for i in range(self.num_processes):
            start = 3 + i * step
            end = min(3 + (i + 1) * step + 2, n)  # запас, щоб не втратити пари
            if start % 2 == 0:
                start += 1
            ranges.append((start, end, None))

        with Pool(processes=self.num_processes) as pool:
            results = pool.map(self._count_pairs, ranges)
            
        total_count = 0
        for count, _ in results:
            total_count += count
            
        return total_count