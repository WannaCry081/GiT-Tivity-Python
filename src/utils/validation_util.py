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
