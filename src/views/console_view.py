class ConsoleView:
    @staticmethod
    def show_main_menu() -> str:
        print("\nОберіть спосіб введення даних:")
        print("1 - Ввести вручну")
        print("2 - Згенерувати випадково")
        print("3 - Зчитати з файлу")
        print("4 - Вийти")
        return input("Ваш вибір: ")

    @staticmethod
    def show_calculation_menu() -> str:
        print("\nОберіть режим обчислення:")
        print("1 - Використовувати багатопоточність")
        print("2 - Звичайне обчислення")
        return input("Ваш вибір: ")

    @staticmethod
    def show_save_menu() -> str:
        print("\nОберіть опцію збереження:")
        print("1 - Зберегти вхідні дані")
        print("2 - Зберегти результат")
        print("3 - Зберегти все")
        print("4 - Не зберігати")
        return input("Ваш вибір: ") 