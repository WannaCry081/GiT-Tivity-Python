import os
import subprocess
from typing import List, Optional


class CommandUtil:
    """
    Utility class for executing shell commands and retrieving Git repository information.
    """
    
    @staticmethod
    def execute_with_result(
        cmd: Optional[str] = None,
        cmd_lst: Optional[List[str]] = None,
    ) -> subprocess.CompletedProcess:
        """
        Executes a shell command and returns the result.

        Args:
            cmd (Optional[str]): A command string to execute.
            cmd_lst (Optional[List[str]]): A command list to execute.

        Returns:
            subprocess.CompletedProcess: The result of the executed command.
        """
        assert (cmd is None) != (
            cmd_lst is None
        ), "Provide either 'cmd' or 'cmd_lst', not both."

        command = cmd.split() if cmd else cmd_lst
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result
        except subprocess.CalledProcessError as e:
            print(f"Command execution failed: {e}")
            return e
          
    @staticmethod
    def get_total_commits() -> int:
        result = CommandUtil.execute_with_result(cmd="git rev-list --count HEAD")
        return int(result.stdout.strip()) if result.returncode == 0 else 0

    @staticmethod
    def get_total_files(directory_path: str) -> int:
        return len(
            [
                f
                for f in os.listdir(directory_path)
                if os.path.isfile(os.path.join(directory_path, f))
            ]
        )