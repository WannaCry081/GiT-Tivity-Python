import argparse
from typing import List


class ArgumentUtil:
    
    @staticmethod
    def parse(arguments: List[str]):
       
        parser = argparse.ArgumentParser(
            description="Configure commit generation settings."
        )

        parser.add_argument(
            "-rc",
            "--random-commits",
            action="store_true",
            help="Randomly distribute commits across days. By default, commits are sequential.",
        )

        parser.add_argument(
            "-nw",
            "--no-weekends",
            action="store_true",
            help="Exclude weekends from commit days (only commit on weekdays).",
        )

        parser.add_argument(
            "-c",
            "--commits",
            type=int,
            default=10,
            help="Number of commits to generate (default: 10).",
        )

        parser.add_argument(
            "-r",
            "--repository",
            type=str,
            help="URL or name of the target GitHub repository (e.g., 'https://github.com/user/repo').",
        )

        return parser.parse_args(arguments)
