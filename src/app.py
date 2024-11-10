import os
import random
import logging
import subprocess
import shutil
from time import sleep
from pathlib import Path
from datetime import datetime
from os.path import dirname, abspath, join
from src.utils import ValidationUtil, CommandUtil, FileUtil, ArgumentUtil

class Program:
    
    @staticmethod
    def commit_changes(commit_message: str) -> None:
        CommandUtil.execute_with_result(cmd="git add .")
        CommandUtil.execute_with_result(cmd_lst=["git", "commit", "-m", commit_message])

    
    @staticmethod
    def setup_project_directory(repository: str | None) -> str:
        if repository != None:
            project_dir = repository.split("/")[-1].replace(".git", "")
        else:
            project_dir = "sample"

        current_dir = abspath(__file__)
        parent_dir = dirname(dirname(dirname(current_dir)))
        os.chdir(parent_dir)

        if not Path(project_dir).exists():
            if repository != None:
                CommandUtil.execute_with_result(cmd=f"git clone {repository}")
            else:
                os.mkdir(project_dir)

        project_dir = join(parent_dir, project_dir)
        os.chdir(project_dir)

        if not Path("README.md").exists():
            shutil.copy(f"{dirname(current_dir)}/static/README.md", project_dir)

        return project_dir
