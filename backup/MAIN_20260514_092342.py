import subprocess

print("===== MAIN START =====")

subprocess.run(
    "py get_ohlc.py",
    shell=True
)

subprocess.run(
    "py upload_github.py",
    shell=True
)

print("===== MAIN END =====")