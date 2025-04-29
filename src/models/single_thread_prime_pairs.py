from sympy import isprime

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