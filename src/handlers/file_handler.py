import json
import os
from typing import Dict, Any

class FileController:
    def save_to_file(self, data: Dict[str, Any], filename: str) -> None:
        try:
            with open(filename, "w", encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"\nДані збережено у файл {filename}")
        except Exception as e:
            print(f"\nПомилка при збереженні файлу: {e}")

    def read_input(self, filename: str) -> int:
        try:
            with open(filename, "r", encoding='utf-8') as f:
                data = json.load(f)
            return data["n"]
        except FileNotFoundError:
            raise ValueError(f"Файл {filename} не знайдено")
        except json.JSONDecodeError:
            raise ValueError(f"Помилка читання файлу {filename}. Неправильний формат JSON")
        except Exception as e:
            raise ValueError(f"Помилка при читанні файлу: {e}") 