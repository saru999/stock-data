import subprocess
import sys

print("===== MAIN START =====")

# Git symbol取得
result = subprocess.run(
    "py get_gitsymbol.py",
    shell=True
)

if result.returncode != 0:

    print(
        "Git symbol取得失敗"
    )

    sys.exit()

# OHLC取得
subprocess.run(
    "py get_ohlc.py",
    shell=True
)

# GitHub upload
subprocess.run(
    "py upload_github.py",
    shell=True
)

print("===== MAIN END =====")