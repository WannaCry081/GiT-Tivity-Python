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


logging.basicConfig(level=logging.INFO)

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

    @staticmethod
    def main(args: list[str]) -> int:
        try:
            arguments = ArgumentUtil.parse(args)
            current_time = datetime.now()
            current_branch = "main" if arguments.repository != None else "master"
            analytics_file_path = "analytics.json"
            project_dir = Program.setup_project_directory(arguments.repository)

            reduction_percentage = random.uniform(0, 0.2)
            total_commits = int(arguments.commits * (1 - reduction_percentage))

            # Check git version and configuration

            if arguments.repository != None:
                CommandUtil.execute_with_result(cmd="git --version")

            user_name = CommandUtil.execute_with_result(
                cmd="git config --global user.name"
            )
            user_email = CommandUtil.execute_with_result(
                cmd="git config --global user.email"
            )

            if ValidationUtil.git_has_config(
                user_name
            ) and ValidationUtil.git_has_config(user_email):
                logging.error("Git configuration for user name and email is required.")
                return -1

            # Initialize Git and set up analytics file if needed
            if not Path(analytics_file_path).exists():
                if not ValidationUtil.git_is_init():
                    CommandUtil.execute_with_result(cmd="git init")

                FileUtil.create_analytics_file(
                    analytics_file_path,
                    git_name=user_name.stdout.strip(),
                    git_email=user_email.stdout.strip(),
                    git_branch=current_branch,
                    no_of_files=1,
                    current_day=str(current_time.date()),
                )
                Program.commit_changes("Initial commit")
                if arguments.repository != None:

                    if not ValidationUtil.git_has_remote():
                        CommandUtil.execute_with_result(
                            cmd=f"git remote add origin {arguments.repository}"
                        )

                    CommandUtil.execute_with_result(
                        cmd=f"git push -u origin {current_branch}"
                    )

            # Load and check analytics file for existing data
            data = FileUtil.open_json_file(analytics_file_path)
            if data:
                updated_at = data["updated_at"]
                no_of_files = data["no_of_files"]

                # Check weekend and random commit conditions
                if arguments.no_weekends and current_time.weekday() >= 5:
                    logging.info("Skipping commits on weekends.")
                    return -1
                if arguments.random_commits and not random.choice([True, False]):
                    logging.info("Randomly skipping commits for today.")
                    return -1
                if updated_at == str(current_time.date()):
                    logging.info("Commits already made for today.")
                    return -1
                if current_time.day == 1:
                    no_of_files += 1
            else:
                logging.warning("Analytics file could not be loaded; starting fresh.")

            # Perform automated commits
            for i in range(total_commits):
                current_time = datetime.now()
                FileUtil.update_fake_file(no_of_files, i, current_time)
                sleep(0.25)
                Program.commit_changes(
                    f"chore: add [{i+1}] contribution {current_time.time()}"
                )

            # Update analytics file after committing
            total_commit_count = CommandUtil.execute_with_result(
                cmd="git rev-list --count HEAD"
            ).stdout.strip()
            FileUtil.update_analytics_file(
                analytics_file_path,
                total_commits=int(total_commit_count),
                no_of_files=no_of_files,
                current_day=str(current_time.date()),
            )
            Program.commit_changes(f"chore: update analytics {current_time.time()}")

            # Push changes if repository is specified
            if arguments.repository != None:
                CommandUtil.execute_with_result(cmd=f"git push origin {current_branch}")

            logging.info("Program execution completed successfully.")

        except FileNotFoundError as e:
            logging.error(
                "File not found: Ensure all paths and files are correctly set.",
                exc_info=True,
            )
            return -1
        except subprocess.CalledProcessError as e:
            logging.error(
                "Command execution failed. Please check Git configuration and repository.",
                exc_info=True,
            )
            return -1
        except Exception as e:
            logging.error("An unexpected error occurred.", exc_info=True)
            return -1

        return 0