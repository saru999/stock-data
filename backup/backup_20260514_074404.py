from pathlib import Path
from datetime import datetime
import shutil
import subprocess

print("===== BACKUP START =====")

# ----------------------------
# backupフォルダ
# ----------------------------

backup_dir = Path("backup")

backup_dir.mkdir(
    exist_ok=True
)

# ----------------------------
# GitHub Private repo
# ----------------------------

private_repo = Path(
    "github_repo/stock-system"
)

# ----------------------------
# backup保存先
# ----------------------------

github_backup_dir = (
    private_repo / "backup"
)

github_backup_dir.mkdir(
    parents=True,
    exist_ok=True
)

# ----------------------------
# 対象ファイル
# ----------------------------

target_files = [
    "get_close.py",
    "upload_github.py",
    "MAIN.py",
    "backup.py"
]

# ----------------------------
# 日付
# ----------------------------

now_str = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)

# ----------------------------
# backup実行
# ----------------------------

for file_name in target_files:

    source = Path(file_name)

    if not source.exists():

        print(f"見つからない: {file_name}")

        continue

    # 拡張子
    stem = source.stem
    suffix = source.suffix

    # backupファイル名
    backup_name = (
        f"{stem}_{now_str}{suffix}"
    )

    # ローカルbackup先
    local_dest = (
        backup_dir / backup_name
    )

    shutil.copy(
        source,
        local_dest
    )

    print(f"local backup: {local_dest}")

    # GitHub backup先
    github_dest = (
        github_backup_dir / backup_name
    )

    shutil.copy(
        source,
        github_dest
    )

    print(f"github backup: {github_dest}")

# ----------------------------
# Git push
# ----------------------------

print("git add")

subprocess.run(
    "git add .",
    cwd=private_repo,
    shell=True
)

print("git commit")

subprocess.run(
    f'git commit -m "backup {now_str}"',
    cwd=private_repo,
    shell=True
)

print("git push")

subprocess.run(
    "git push",
    cwd=private_repo,
    shell=True
)

print("===== BACKUP END =====")