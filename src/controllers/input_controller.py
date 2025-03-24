import random
from dataclasses import dataclass

@dataclass
class InputData:
    value: int
    source: str

class InputController:
    @staticmethod
    def get_manual_input() -> InputData:
        n = int(input("Введіть значення n: "))
        return InputData(n, "manual")

    @staticmethod
    def generate_random_input() -> InputData:
        max_value = int(input("Введіть максимальне значення n для генерації: "))
        n = random.randint(1, max_value)
        return InputData(n, "random") 