import comtypes.client

prices = comtypes.client.CreateObject("ActiveMarket.Prices")

prices.Read("3038", 0.0, 0.0)

begin = prices.Begin()
end = prices.End()

print("begin =", begin)
print("end =", end)

for pos in range(end - 10, end + 1):

    print(
        pos,
        prices.Open(pos),
        prices.High(pos),
        prices.Low(pos),
        prices.Close(pos),
        prices.Volume(pos)
    )