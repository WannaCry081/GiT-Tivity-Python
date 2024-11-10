import subprocess


class CommandUtil:
  
    @staticmethod
    def execute_with_result(
        cmd: Optional[str] = None,
        cmd_lst: Optional[List[str]] = None,
    ) -> subprocess.CompletedProcess:
      
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