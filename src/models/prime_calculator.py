from sympy import isprime
from concurrent.futures import ThreadPoolExecutor
from math import ceil
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class CalculationResult:
    count: int
    pairs: List[Tuple[int, int]]
    execution_time: float
    mode: str

class PrimeCalculator:
    def __init__(self):
        self.num_threads = 4

    def _find_prime_pairs_in_range(self, start: int, end: int) -> List[Tuple[int, int]]:
        primes = [i for i in range(start, end, 2) if isprime(i)]
        prime_pairs = [(primes[i], primes[i + 1]) 
                      for i in range(len(primes) - 1) 
                      if primes[i + 1] - primes[i] == 2]
        return prime_pairs

    def calculate_parallel(self, n: int) -> List[Tuple[int, int]]:
        chunk_size = ceil((n - 3) / self.num_threads)
        ranges = []
        
        start = 3
        while start < n:
            end = min(start + chunk_size, n)
            if start % 2 == 0:
                start += 1
            ranges.append((start, end))
            start += chunk_size

        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            results = list(executor.map(
                lambda r: self._find_prime_pairs_in_range(*r), ranges))

        all_pairs = []
        for pairs in results:
            all_pairs.extend(pairs)

        return sorted(list(set(all_pairs)))

    def calculate_single(self, n: int) -> List[Tuple[int, int]]:
        return self._find_prime_pairs_in_range(3, n) 