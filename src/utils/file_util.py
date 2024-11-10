import json
from typing import Optional


class FileUtil:

    @staticmethod
    def open_json_file(file_name: str) -> Optional[dict]:
        with open(file_name, "r") as file:
            return json.load(file)
