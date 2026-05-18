import subprocess
from pathlib import Path
import shutil

print(
    "===== GitHub Upload START ====="
)

# outputフォルダ
output_dir = Path(
    "output"
)

# 最新CSV取得
csv_files = list(
    output_dir.glob("*.csv")
)

if not csv_files:

    print(
        "CSVがありません"
    )

    exit()

latest_file = max(
    csv_files,
    key=lambda x: x.stat().st_mtime
)

print(
    "最新CSV"
)

print(
    latest_file
)

# project直下へコピー
destination = Path(
    latest_file.name
)

shutil.copy(
    latest_file,
    destination
)

print(
    "コピー完了"
)

# add
subprocess.run(
    "git add .",
    shell=True
)

# commit
subprocess.run(
    f'git commit -m "daily update {latest_file.name}"',
    shell=True
)

# pull（重要）
print(
    "Git pull 実行"
)

result = subprocess.run(
    "git pull --rebase origin main",
    shell=True
)

if result.returncode != 0:

    print(
        "git pull失敗"
    )

    exit()

# push
print(
    "Git push 実行"
)

result = subprocess.run(
    "git push origin main",
    shell=True
)

if result.returncode == 0:

    print(
        "GitHub push 完了"
    )

else:

    print(
        "GitHub push 失敗"
    )

print(
    "===== GitHub Upload END ====="
)