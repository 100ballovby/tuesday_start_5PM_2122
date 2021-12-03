currencies = ['EUR', 'GBP', 'RUB', 'BYN', 'AED', 'JY', 'BTC']
rates = [0.88, 0.74, 75.56, 2.6, 3.67, 133.37, 0.010018]
exchange = {}

for index in range(len(currencies)):
    exchange[currencies[index]] = rates[index]

print(exchange)

