import os
import datetime
import subprocess
import math

# Beautiful beach sunset pattern (7 rows x 52 columns)
PATTERN = [[0 for _ in range(52)] for _ in range(7)]

# Light sky (top 3 rows)
for col in range(52):
    for row in range(3):
        PATTERN[row][col] = 1

# Large setting sun with glow (center around row 2, col 15)
sun_row = 2
sun_col = 15
sun_radius = 3
for row in range(7):
    for col in range(52):
        dist = math.sqrt((row - sun_row)**2 + (col - sun_col)**2)
        if dist < sun_radius:
            PATTERN[row][col] = max(PATTERN[row][col], 3)  # bright sun
        elif dist < sun_radius + 2:
            PATTERN[row][col] = max(PATTERN[row][col], 2)  # warm glow

# Calm ocean (rows 3-4)
for col in range(52):
    for row in range(3, 5):
        PATTERN[row][col] = 2

# Golden sun reflection on water
for col in range(10, 21):
    PATTERN[4][col] = 1

# Sandy beach (bottom 2 rows)
for col in range(52):
    for row in range(5, 7):
        PATTERN[row][col] = 3

# Palm tree silhouette on the right
# Trunk
for row in range(2, 7):
    PATTERN[row][45] = 3
    PATTERN[row][46] = 3

# Fronds
PATTERN[0][43:49] = [2] * 6
PATTERN[1][42:44] = [2] * 2
PATTERN[1][47:50] = [2] * 3
PATTERN[2][41] = 2
PATTERN[2][49] = 2

# Birds flying in the sky
PATTERN[1][5] = 3
PATTERN[1][7] = 3
PATTERN[2][6] = 3

PATTERN[1][30] = 3
PATTERN[1][32] = 3
PATTERN[2][31] = 3

# Commit levels (low total commits ~450-500)
COMMITS_PER_LEVEL = {0: 0, 1: 1, 2: 3, 3: 5}

# First day of 2022 was Saturday, Jan 1, 2022
FIRST_DAY = datetime.date(2022, 1, 1)

def init_repo():
    subprocess.call(["git", "init"])
    with open("art.txt", "w") as f:
        f.write("Beautiful beach sunset pixel art for 2022\n")
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
            f.write(f"Sunset commit {i+1} on {commit_date}\n")
        subprocess.call(["git", "add", "art.txt"])
        subprocess.call(["git", "commit", "-m", f"Art on {commit_date}"], env=env)

init_repo()

# Generate commits across 52 weeks
for col in range(52):
    for row in range(7):
        level = PATTERN[row][col]
        target_commits = COMMITS_PER_LEVEL[level]
        if target_commits == 0:
            continue
        
        delta_days = col * 7 + row
        commit_date = FIRST_DAY + datetime.timedelta(days=delta_days)
        
        if commit_date.year != 2022:
            continue
            
        make_commits_on_date(commit_date, target_commits)

print("Beach sunset art commits complete! 🌅🏖️")
print("Create a new empty repo on GitHub, add remote, and push.")
print("The heatmap will update in a few hours – enjoy your serene sunset!")