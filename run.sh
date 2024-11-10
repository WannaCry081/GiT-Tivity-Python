#!/bin/bash
# -----------------------------------------------------------------------------
# GitHub Activity Generator - Run Script
# -----------------------------------------------------------------------------
# Author: WannaCry081
# Email: liraedata59@gmail.com
# Description: This script runs the GitHub Activity Generator, allowing you to
#              generate fake commits to simulate contribution activity on GitHub.
# -----------------------------------------------------------------------------

echo """
 ██████╗ ██╗████████╗████████╗██╗██╗   ██╗██╗████████╗██╗   ██╗
██╔════╝ ██║╚══██╔══╝╚══██╔══╝██║██║   ██║██║╚══██╔══╝╚██╗ ██╔╝
██║  ███╗██║   ██║█████╗██║   ██║██║   ██║██║   ██║    ╚████╔╝ 
██║   ██║██║   ██║╚════╝██║   ██║╚██╗ ██╔╝██║   ██║     ╚██╔╝  
╚██████╔╝██║   ██║      ██║   ██║ ╚████╔╝ ██║   ██║      ██║   
 ╚═════╝ ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═══╝  ╚═╝   ╚═╝      ╚═╝   
"""

# Run the main script with 20 commits as default
echo "Running GitHub Activity Generator..."
python main.py --commits=20

echo "Script execution completed."
