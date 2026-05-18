import csv
from pathlib import Path
from datetime import datetime
import random
import shutil

import comtypes.client

print("===== GET OHLC START =====")

# ----------------------------
# 設定
# ----------------------------

# True  = ランダムテスト
# False = ChartGallery実取得
USE_RANDOM = False

# ----------------------------
# 現在フォルダ
# ----------------------------

print("現在フォルダ")
print(Path.cwd())

# ----------------------------
# symbol.csv
# ----------------------------

symbol_file = Path("symbol.csv")

if not symbol_file.exists():

    print("symbol.csv が見つかりません")

    exit()

# ----------------------------
# symbol読込
# ----------------------------

symbols = []

with open(
    symbol_file,
    "r",
    encoding="utf-8"
) as f:

    reader = csv.DictReader(f)

    for row in reader:

        symbol = row["symbol"].strip()

        if symbol:

            symbols.append(symbol)

print("読込symbol")
print(symbols)

# ----------------------------
# 昇順ソート
# ----------------------------

symbols.sort()

# ----------------------------
# ChartGallery接続
# ----------------------------

prices = None

if not USE_RANDOM:

    try:

        prices = (
            comtypes.client.CreateObject(
                "ActiveMarket.Prices"
            )
        )

        print(
            "ChartGallery接続成功"
        )

    except Exception as e:

        print(
            "ChartGallery接続失敗"
        )

        print(e)

        print(
            "ランダムモードへ切替"
        )

        USE_RANDOM = True

# ----------------------------
# 出力用
# ----------------------------

result_rows = []

# ----------------------------
# 株価取得
# ----------------------------

for symbol in symbols:

    try:

        # =====================================
        # ChartGallery 実取得
        # =====================================

        if not USE_RANDOM:

            prices.Read(
                symbol,
                0.0,
                0.0
            )

            begin = (
                prices.Begin()
            )

            end = (
                prices.End()
            )

            # 最新営業日
            pos = end

            open_price = int(
                prices.Open(pos)
            )

            high_price = int(
                prices.High(pos)
            )

            low_price = int(
                prices.Low(pos)
            )

            close_price = int(
                prices.Close(pos)
            )

            volume = int(
                prices.Volume(pos)
            )

        # =====================================
        # テスト用ランダム
        # =====================================

        else:

            open_price = (
                random.randint(
                    1000,
                    5000
                )
            )

            high_price = (
                open_price +
                random.randint(
                    0,
                    300
                )
            )

            low_price = (
                open_price -
                random.randint(
                    0,
                    300
                )
            )

            close_price = (
                random.randint(
                    low_price,
                    high_price
                )
            )

            volume = (
                random.randint(
                    10000,
                    5000000
                )
            )

        # ----------------------------
        # print
        # ----------------------------

        print(
            f"{symbol} "
            f"O:{open_price} "
            f"H:{high_price} "
            f"L:{low_price} "
            f"C:{close_price} "
            f"V:{volume}"
        )

        # ----------------------------
        # 保存
        # ----------------------------

        result_rows.append({

            "symbol":
                symbol,

            "open":
                open_price,

            "high":
                high_price,

            "low":
                low_price,

            "close":
                close_price,

            "volume":
                volume
        })

    except Exception as e:

        print(
            f"{symbol} "
            f"取得失敗"
        )

        print(e)

# ----------------------------
# output
# ----------------------------

output_dir = Path(
    "output"
)

output_dir.mkdir(
    exist_ok=True
)

# ----------------------------
# 日付
# ----------------------------

today = (
    datetime.now()
    .strftime("%Y%m%d")
)

# ----------------------------
# 保存先
# ----------------------------

output_file = (
    output_dir /
    f"{today}_ohlc.csv"
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

    writer.writerows(
        result_rows
    )

print("CSV保存完了")
print(output_file)

# ----------------------------
# latest_ohlc.csv
# ----------------------------

latest_file = (
    output_dir /
    "latest_ohlc.csv"
)

shutil.copy(
    output_file,
    latest_file
)

print(
    "latest_ohlc.csv 更新完了"
)

print(
    "===== GET OHLC END ====="
)