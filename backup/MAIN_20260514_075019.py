import subprocess

print("===== MAIN START =====")

# ----------------------------
# 株価取得
# ----------------------------

print("get_close.py 実行")

subprocess.run(
    ["py", "get_close.py"]
)

# ----------------------------
# GitHub upload
# ----------------------------

print("upload_github.py 実行")

subprocess.run(
    ["py", "upload_github.py"]
)

print("===== MAIN END =====")