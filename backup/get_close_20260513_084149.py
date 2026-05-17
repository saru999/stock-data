import csv
from pathlib import Path
from datetime import datetime
import random

print("===== GET CLOSE START =====")

# ----------------------------
# 現在フォルダ表示
# ----------------------------

print("現在フォルダ")
print(Path.cwd())

# ----------------------------
# symbol.csv 読込
# ----------------------------

symbols = []

with open(
    "symbol.csv",
    "r",
    encoding="utf-8"
) as f:

    reader = csv.DictReader(f)

    for row in reader:

        symbols.append(
            row["symbol"]
        )

print("読込symbol")
print(symbols)

# ----------------------------
# ソート
# ----------------------------

symbols.sort()

print("ソート後")
print(symbols)

# ----------------------------
# 株価取得
# （現在はダミー）
# ----------------------------

results = []

for symbol in symbols:

    # 仮価格
    close_price = random.randint(
        1000,
        15000
    )

    print(
        f"{symbol} -> {close_price}"
    )

    results.append(
        [
            symbol,
            close_price
        ]
    )

# ----------------------------
# outputフォルダ
# ----------------------------

output_dir = Path("output")

output_dir.mkdir(
    exist_ok=True
)

# ----------------------------
# 出力ファイル名
# ----------------------------

today_str = datetime.now().strftime(
    "%Y%m%d"
)

output_file = (
    output_dir /
    f"{today_str}_close.csv"
)

# ----------------------------
# CSV保存
# ----------------------------

with open(
    output_file,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)

    writer.writerow(
        [
            "symbol",
            "close"
        ]
    )

    writer.writerows(results)

print("保存先")
print(output_file)

print("CSV保存完了")

print("===== GET CLOSE END =====")