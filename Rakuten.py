import win32com.client

prices = win32com.client.gencache.EnsureDispatch("ActiveMarket.Prices")

help(prices.Read)