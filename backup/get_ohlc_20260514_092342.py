import csv
from datetime import datetime
from pathlib import Path
import random

print("===== GET OHLC START =====")

# symbol.csv
symbol_file = Path("symbol.csv")

if not symbol_file.exists():

    print("symbol.csv が見つかりません")

    exit()

# symbol読込
symbols = []

with open(
    symbol_file,
    "r",
    encoding="utf-8"
) as f:

    reader = csv.DictReader(f)

    for row in reader:

        symbol = row["symbol"].strip()

        symbols.append(symbol)

print("読込symbol")
print(symbols)

# 昇順
symbols.sort()

# 出力用
result_rows = []

for symbol in symbols:

    # 本来はChartGalleryから取得
    # 今回はサンプル値

    open_price = random.randint(1000, 5000)

    high_price = open_price + random.randint(0, 300)

    low_price = open_price - random.randint(0, 300)

    close_price = random.randint(
        low_price,
        high_price
    )

    volume = random.randint(
        10000,
        5000000
    )

    print(
        f"{symbol} "
        f"O:{open_price} "
        f"H:{high_price} "
        f"L:{low_price} "
        f"C:{close_price}"
    )

    result_rows.append({
        "symbol": symbol,
        "open": open_price,
        "high": high_price,
        "low": low_price,
        "close": close_price,
        "volume": volume
    })

# output
output_dir = Path("output")

output_dir.mkdir(
    exist_ok=True
)

# YYYYMMDD
today = datetime.now().strftime(
    "%Y%m%d"
)

output_file = (
    output_dir /
    f"{today}_ohlc.csv"
)

# CSV保存
with open(
    output_file,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=[
            "symbol",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]
    )

    writer.writeheader()

    writer.writerows(result_rows)

print("CSV保存完了")

print(output_file)

print("===== GET OHLC END =====")