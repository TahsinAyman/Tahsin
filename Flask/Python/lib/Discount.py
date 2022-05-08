def dis(price, discount):
    return round(price - (price * (discount / 100)), 2)


print(dis(200.345, 75.5))
