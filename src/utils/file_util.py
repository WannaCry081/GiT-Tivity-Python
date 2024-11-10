import json
from typing import Optional


class FileUtil:

    @staticmethod
    def open_json_file(file_name: str) -> Optional[dict]:
        with open(file_name, "r") as file:
            return json.load(file)

    @staticmethod
    def create_analytics_file(file_name: str, **kwargs) -> None:
        resource = {
            "git": {
                "name": kwargs["git_name"],
                "email": kwargs["git_email"],
                "branch": kwargs["git_branch"],
            },
            "no_of_commits": 1,
            "no_of_files": kwargs["no_of_files"],
            "created_at": kwargs["current_day"],
            "updated_at": "",
        }

        with open(file_name, "w") as file:
            json.dump(resource, file, indent=4)

