import win32com.client

names = win32com.client.Dispatch("ActiveMarket.Names")

codes, stocknames = names.AllNames(1)

for i in range(10):
    print(codes[i], stocknames[i])