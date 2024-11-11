import argparse
from typing import List


class ArgumentUtil:
    """
    Utility class to parse command-line arguments for configuring commit distribution and repository settings.
    """

    @staticmethod
    def parse(arguments: List[str]):
        """
        Parses command-line arguments for the contribution activity generator.

        Args:
            arguments (List[str]): A list of command-line arguments.

        Returns:
            Namespace: An argparse.Namespace containing the parsed arguments.
        """
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
            "-l",
            "--local",
            action="store_true",
            help="Configure if the repository is local",
        )

        parser.add_argument(
            "-r",
            "--repository",
            required=True,
            type=str,
            help="URL or name of the target GitHub repository (e.g., 'https://github.com/user/repo').",
        )

        return parser.parse_args(arguments)
