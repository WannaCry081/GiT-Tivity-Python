from src.utils import CommandUtil


class Program:
    
    @staticmethod
    def commit_changes(commit_message: str) -> None:
        CommandUtil.execute_with_result(cmd="git add .")
        CommandUtil.execute_with_result(cmd_lst=["git", "commit", "-m", commit_message])
