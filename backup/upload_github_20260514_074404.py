from pathlib import Path
import shutil
import subprocess
from datetime import datetime

print("===== GitHub Upload START =====")

# ----------------------------
# GitHub clone先
# ----------------------------

github_repo = Path(
    r"github_repo\stock-data"
)

# ----------------------------
# outputフォルダ
# ----------------------------

output_dir = Path("output")

# ----------------------------
# CSV一覧取得
# ----------------------------

csv_files = sorted(
    output_dir.glob("*_close.csv")
)

if not csv_files:

    print("CSVファイルがありません")
    exit()

# ----------------------------
# 最新CSV
# ----------------------------

latest_file = csv_files[-1]

print("最新CSV")
print(latest_file)

# ----------------------------
# 日付CSVコピー
# ----------------------------

dest_file = (
    github_repo /
    latest_file.name
)

print("コピー先")
print(dest_file)

shutil.copy(
    latest_file,
    dest_file
)

print("日付CSVコピー完了")

# ----------------------------
# latest_close.csv 更新
# ----------------------------

latest_dest = (
    github_repo /
    "latest_close.csv"
)

shutil.copy(
    latest_file,
    latest_dest
)

print("latest_close.csv 更新完了")

# ----------------------------
# upload_log.txt 更新
# ----------------------------

log_file = (
    github_repo /
    "upload_log.txt"
)

now_str = datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S"
)

with open(
    log_file,
    "a",
    encoding="utf-8"
) as f:

    f.write(
        f"{now_str} upload {latest_file.name}\n"
    )

print("upload_log.txt 更新完了")

# ----------------------------
# git add
# ----------------------------

print("git add")

subprocess.run(
    ["git", "add", "."],
    cwd=github_repo
)

# ----------------------------
# git commit
# ----------------------------

print("git commit")

commit_message = (
    f"daily update {latest_file.name}"
)

subprocess.run(
    [
        "git",
        "commit",
        "-m",
        commit_message
    ],
    cwd=github_repo
)

# ----------------------------
# git push
# ----------------------------

print("git push")

subprocess.run(
    ["git", "push"],
    cwd=github_repo
)

print("GitHub push 完了")

print("===== GitHub Upload END =====")