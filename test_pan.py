import win32com.client

# PanRolling COM接続
names = win32com.client.Dispatch("ActiveMarket.Names")

# 銘柄一覧取得
codes, stocknames = names.AllNames(1)

# 最初の20件表示
for i in range(20):
    print(codes[i], stocknames[i])