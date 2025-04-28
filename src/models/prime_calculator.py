from sympy import isprime
from concurrent.futures import ThreadPoolExecutor

class SingleThreadPrimePairs:
    def calculate(self, n: int) -> int:
        count = 0
        last_prime = None
        i = 3
        while i < n:
            if isprime(i):
                if last_prime is not None and i - last_prime == 2:
                    count += 1
                last_prime = i
                i += 2
            else:
                i += 2 
        return count

class MultiThreadPrimePairs:
    def __init__(self, num_threads: int = 4):
        self.num_threads = num_threads

    def _count_pairs(self, start: int, end: int, prev_prime: int = None) -> (int, int):
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
        step = (n - 3) // self.num_threads + 1
        ranges = []
        for i in range(self.num_threads):
            start = 3 + i * step
            end = min(3 + (i + 1) * step + 2, n)  # запас, щоб не втратити пари
            if start % 2 == 0:
                start += 1
            ranges.append((start, end))

        results = []
        prev_last_prime = None
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            futures = []
            for r in ranges:
                futures.append(executor.submit(self._count_pairs, r[0], r[1], prev_last_prime))
            prev_last_prime = None
            for f in futures:
                res, prev_last_prime = f.result()
                results.append(res)
        return sum(results)
