stock_prices = []
with open ("stock_prices.csv") as f:
    for line in f:
        tokens=line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])

print(stock_prices)

for elem in stock_prices:
    if elem[0]=="9 Mar":
        print(elem[1])