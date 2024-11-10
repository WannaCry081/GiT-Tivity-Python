# 🤖 GitHub Contribution Activity Generator

A simple Python tool that simulates GitHub contributions by generating fake commits for a GitHub repository. It can generate random commits, exclude weekends, and track analytics for each contribution activity.

## ✨ Features

- **Generate Random Commits**: Simulate contributions with random commit dates.
- **Exclude Weekends**: Option to exclude commits on weekends.
- **Track Analytics**: Track the number of commits and files in a `analytics.json` file.
- **Push to GitHub**: Automatically push commits to your GitHub repository.
- **Customizable Commits**: Control the number of commits to be made and the repository to which they will be pushed.

## 📦 Requirements

- Python 3.x
- Git installed and configured on your machine
- A GitHub repository (optional if using an existing repo)

## 💻 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/github-contribution-generator.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute the script:

   ```bash
   python main.py --random-commits --no-weekends --commits 20 --repository https://github.com/username/repo

   ```

4. Alternatively, modify the `run.sh` script and execute it:

   ```bash
   ./run.sh
   ```

## 🎊 Usage

### Command-Line Arguments

| Argument                   | Description                                                            |
| -------------------------- | ---------------------------------------------------------------------- |
| `-rc` / `--random-commits` | Enable random commit distribution (default: `False`)                   |
| `-nw` / `--no-weekends`    | Exclude weekends from commit days (default: `False`)                   |
| `-c` / `--commits`         | Specify the number of commits to generate (default: `10`)              |
| `-r` / `--repository`      | GitHub repository URL (e.g., `https://github.com/username/repository`) |

### Example Usage

1. **Generate 10 commits and push to GitHub**:

   ```bash
   python main.py --commits 10 --repository https://github.com/yourusername/yourrepository
   ```

2. **Generate random commits and exclude weekends**:

   ```bash
   python main.py --random-commits --no-weekends --commits 5 --repository https://github.com/yourusername/yourrepository
   ```

3. **Run with default settings (10 commits, no repository specified)**:
   ```bash
   python main.py
   ```

## 🚀 How It Works

1. **Git Configuration**: The tool checks for a valid Git configuration (user name and email). If not configured, it prompts the user to initialize Git.
2. **Commit Generation**: Based on the user input (number of commits, random distribution, weekend exclusion), it generates commits in the repository.
3. **Analytics**: It tracks the number of commits and files in a `analytics.json` file. This file is updated after each commit activity.
4. **Push to GitHub**: After generating commits locally, it pushes the changes to the specified GitHub repository.

## Example Output

```bash
Commit 1: chore: add [1] contribution 2024-11-10 10:30:15
Commit 2: chore: add [2] contribution 2024-11-10 10:30:30
...
Finish executing program
```

The tool will output logs for each commit, indicating the date, time, and a description of the commit.

## 🤝 Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -am 'Add new feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Create a new Pull Request for review.

## 📬 Contact

For any questions or feedback, feel free to reach out:

- **Email:** liraedata59@gmail.com
- **GitHub:** [WannaCry081](https://github.com/WannaCry081)
