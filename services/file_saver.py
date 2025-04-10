import json
import os
from collections import deque
from settings import config


class JSONSaver:
    def __init__(self):
        self.data = self.load_from_json()

    def save_to_json(self):
        if not self.data:
            return
        serializable_data = {key: list(value) for key, value in self.data.items()}
        with open(
            os.path.join(config.BASE_DIR, config.FILE_NAME), "w", encoding="utf-8"
        ) as file:
            json.dump(serializable_data, file, indent=4)

    def load_from_json(self):
        try:
            with open(
                os.path.join(config.BASE_DIR, config.FILE_NAME), "r", encoding="utf-8"
            ) as file:
                loaded_data = json.load(file)
                data = {
                    int(key): deque(value, maxlen=10)
                    for key, value in loaded_data.items()
                }
                return data
        except FileNotFoundError:
            return {}

    def add_to_json(self, key, value):
        if key not in self.data:
            self.data[key] = deque(maxlen=10)
        self.data[key].appendleft(value)
        self.save_to_json()
