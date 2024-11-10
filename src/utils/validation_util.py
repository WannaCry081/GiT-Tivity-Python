import subprocess
from pathlib import Path
from typing import Optional

class ValidationUtil:
    """
    Utility class for validating Git configurations and repository state.
    """

    @staticmethod
    def git_is_init() -> bool:
        """
        Checks if the current directory is a Git repository.

        Returns:
            bool: True if the current directory is a Git repository, False otherwise.
        """
        return Path(".git").exists()

    @staticmethod
    def git_has_config(result: str) -> Optional[bool]:
        """
        Checks if a Git configuration value is set.

        Args:
            result (str): The output from a Git configuration check command.

        Returns:
            Optional[bool]: True if the configuration value is present, None if it is empty or missing.
        """
        value = result.strip() if isinstance(result, str) else ""
        return bool(value) if value else None

    @staticmethod
    def git_has_remote() -> bool:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        return True if result.returncode == 0 else False
