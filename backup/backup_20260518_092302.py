from pathlib import Path
from datetime import datetime
import shutil
import subprocess
import re

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
# MAIN.py 読込
# ----------------------------

main_file = Path(
    "MAIN.py"
)

if not main_file.exists():

    print(
        "MAIN.py が見つかりません"
    )

    exit()

main_text = main_file.read_text(
    encoding="utf-8"
)

# ----------------------------
# py xxxx.py を抽出
# ----------------------------

matches = re.findall(
    r'py\s+([a-zA-Z0-9_]+\.py)',
    main_text
)

# 重複除去
target_files = list(
    set(matches)
)

# ----------------------------
# 固定ファイル追加
# ----------------------------

fixed_files = [

    "MAIN.py",
    "backup.py",
    "run_MAIN.bat",
    "symbol.csv"
]

for file_name in fixed_files:

    if file_name not in target_files:

        target_files.append(
            file_name
        )

print("backup対象")

for file in target_files:

    print(file)

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

        print(
            f"見つからない: "
            f"{file_name}"
        )

        continue

    stem = source.stem
    suffix = source.suffix

    backup_name = (
        f"{stem}_"
        f"{now_str}"
        f"{suffix}"
    )

    # local backup
    local_dest = (
        backup_dir /
        backup_name
    )

    shutil.copy(
        source,
        local_dest
    )

    print(
        f"local backup: "
        f"{local_dest}"
    )

    # github backup
    github_dest = (
        github_backup_dir /
        backup_name
    )

    shutil.copy(
        source,
        github_dest
    )

    print(
        f"github backup: "
        f"{github_dest}"
    )

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