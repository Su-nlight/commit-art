import os
import datetime
import subprocess

# DNA double helix pattern (7 rows x 52 columns)
PATTERN = []
for row in range(7):
    line = []
    for col in range(52):
        # Twisting strands and rungs
        if (col + row) % 8 == 0 or (col - row) % 8 == 4:
            line.append(3)  # dark strand
        elif (col + row) % 8 == 1 or (col - row) % 8 == 3:
            line.append(2)  # medium rungs
        elif (col + row) % 8 == 2 or (col - row) % 8 == 2:
            line.append(1)  # light strand
        else:
            line.append(0)
    PATTERN.append(line)

# Commit counts (low total ~500 commits)
COMMITS_PER_LEVEL = {0: 0, 1: 1, 2: 3, 3: 5}

START_COL = 1
FIRST_DAY = datetime.date(2023, 1, 1)  # Sunday

def init_repo():
    subprocess.call(["git", "init"])
    with open("art.txt", "w") as f:
        f.write("DNA double helix pixel art for 2023\n")
    subprocess.call(["git", "add", "art.txt"])
    subprocess.call(["git", "commit", "-m", "Initial commit"])

def make_commits_on_date(commit_date, num_commits):
    if num_commits == 0:
        return
    date_str = commit_date.strftime("%Y-%m-%dT12:00:00")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    
    for i in range(num_commits):
        with open("art.txt", "a") as f:
            f.write(f"DNA commit {i+1} on {commit_date}\n")
        subprocess.call(["git", "add", "art.txt"])
        subprocess.call(["git", "commit", "-m", f"Art on {commit_date}"], env=env)

init_repo()

for col in range(52):
    for row in range(7):
        level = PATTERN[row][col]
        target_commits = COMMITS_PER_LEVEL[level]
        if target_commits == 0:
            continue
        
        delta_days = col * 7 + row
        commit_date = FIRST_DAY + datetime.timedelta(days=delta_days)
        
        if commit_date.year != 2023:
            continue
            
        make_commits_on_date(commit_date, target_commits)

print("DNA helix art commits complete! 🧬")
print("Push to a new empty GitHub repo to see the twisting double helix on your 2023 heatmap.")