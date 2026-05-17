from pathlib import Path
import shutil
import subprocess

print("===== GitHub Upload START =====")

# output
output_dir = Path("output")

# 最新CSV
csv_files = sorted(
    output_dir.glob("*_ohlc.csv")
)

latest_file = csv_files[-1]

print("最新CSV")
print(latest_file)

# repo
repo_dir = Path(
    "github_repo/stock-data"
)

# コピー先
dest_file = (
    repo_dir / latest_file.name
)

# コピー
shutil.copy(
    latest_file,
    dest_file
)

print("コピー完了")

# latest_ohlc.csv
latest_dest = (
    repo_dir / "latest_ohlc.csv"
)

shutil.copy(
    latest_file,
    latest_dest
)

# git add
subprocess.run(
    "git add .",
    cwd=repo_dir,
    shell=True
)

# git commit
subprocess.run(
    f'git commit -m "daily update {latest_file.name}"',
    cwd=repo_dir,
    shell=True
)

# git push
subprocess.run(
    "git push",
    cwd=repo_dir,
    shell=True
)

print("GitHub push 完了")