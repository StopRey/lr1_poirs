import time
from src.controllers.input_controller import InputController
from src.controllers.file_controller import FileController
from src.models.prime_calculator import PrimeCalculator
from src.views.console_view import ConsoleView

class Application:
    def __init__(self):
        self.view = ConsoleView()
        self.calculator = PrimeCalculator()
        self.input_controller = InputController()
        self.file_controller = FileController()

    def run(self):
        while True:
            choice = self.view.show_main_menu()

            if choice == "4":
                print("\nВихід з програми.")
                break

            try:
                n = self._handle_input(choice)
                if n is None:
                    continue

                calc_choice = self.view.show_calculation_menu()
                result = self._perform_calculation(n, calc_choice)
                self._handle_saving(choice, n, result)

            except ValueError as e:
                print(f"\nПомилка: {e}")
                continue

    def _handle_input(self, choice):
        if choice == "1":
            return self.input_controller.get_manual_input().value
        elif choice == "2":
            input_data = self.input_controller.generate_random_input()
            print(f"Згенероване значення n: {input_data.value}")
            return input_data.value
        elif choice == "3":
            filename = input("Введіть назву файлу: ")
            return self.file_controller.read_input(filename)
        else:
            print("Невірний вибір! Спробуйте ще раз.")
            return None

    def _perform_calculation(self, n, calc_choice):
        start_time = time.time()
        if calc_choice == "1":
            pairs = self.calculator.calculate_parallel(n)
            mode = "багатопотоковий"
        else:
            pairs = self.calculator.calculate_single(n)
            mode = "звичайний"
        
        elapsed_time = time.time() - start_time
        count = len(pairs)

        print(f"\nРежим обчислення: {mode}")
        print(f"Кількість послідовних простих пар: {count}")
        print(f"Час виконання: {elapsed_time:.6f} секунд")

        return {
            "result": count,
            "time": elapsed_time,
            "prime_pairs": pairs,
            "mode": mode
        }

    def _handle_saving(self, input_choice, n, result):
        if input_choice in ["1", "2", "3"]:
            save_choice = self.view.show_save_menu()
            
            if save_choice == "1":
                self.file_controller.save_to_file({"n": n}, "saves/input.json")
            elif save_choice == "2":
                self.file_controller.save_to_file(result, "saves/output.json")
            elif save_choice == "3":
                self.file_controller.save_to_file({"n": n}, "saves/input.json")
                self.file_controller.save_to_file(result, "saves/output.json")

if __name__ == "__main__":
    app = Application()
    app.run() 