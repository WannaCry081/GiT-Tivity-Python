import json
from datetime import datetime
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

    @staticmethod
    def update_fake_file(
        no_reference: int, counter: int, current_time: datetime
    ) -> None:
        
        with open(f"[{no_reference}]-contributions.txt", "a+") as file:
            if counter == 0:
                file.write(f"{'=' * 20} {current_time.date()} {'=' * 20}\n")
            file.write(
                f"[{counter+1}] Contributions: {current_time.hour}:{current_time.minute}:{current_time.second}:{current_time.microsecond}\n"
            )

    @staticmethod
    def update_analytics_file(file_name: str, **kwargs) -> None:

        with open(file_name, "r") as rfile:
            settings = json.load(rfile)

        settings["no_of_commits"] = kwargs["total_commits"]
        settings["no_of_files"] = kwargs["no_of_files"]
        settings["updated_at"] = kwargs["current_day"]

        with open(file_name, "w") as wfile:
            json.dump(settings, wfile, indent=4)
