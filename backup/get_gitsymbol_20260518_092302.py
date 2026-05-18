import requests
from pathlib import Path

from config import (
    GITHUB_SYMBOL_URL
)

print(
    "===== GET GIT SYMBOL START ====="
)

save_file = Path(
    "symbol.csv"
)

try:

    response = requests.get(
        GITHUB_SYMBOL_URL
    )

    response.raise_for_status()

    save_file.write_bytes(
        response.content
    )

    print(
        "symbol.csv 更新完了"
    )

except Exception as e:

    print(
        "取得失敗"
    )

    print(e)

    exit()

print(
    "===== GET GIT SYMBOL END ====="
)