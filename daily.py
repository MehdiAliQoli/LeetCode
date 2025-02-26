import os
import subprocess
import datetime

# Set your repository path
repo_path = 'C:\Users\DANISH LAPTOP\OneDrive\Desktop\dailygit\LeetCode'

# Navigate to the repository
os.chdir(repo_path)

# Generate a simple Python file
file_name = 'daily_commit.py'
with open(file_name, 'w') as f:
    f.write("# This is a simple daily commit file\n")
    f.write(f"# Created on {datetime.datetime.now()}\n")
    f.write("print('Hello, GitHub!')\n")

# Git commands to add, commit, and push changes
subprocess.run(['git', 'add', file_name])
commit_message = f'Daily commit {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
subprocess.run(['git', 'commit', '-m', commit_message])
subprocess.run(['git', 'push'])

# Delete the file after pushing
os.remove(file_name)

print('Daily commit completed and file deleted.')
