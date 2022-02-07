def calculatePrice(valueOfGoods, discount, shippingCost):
    print(valueOfGoods - valueOfGoods * discount/100 + shippingCost)


# Valid EC
calculatePrice(1000, 10, 19)  #T1
calculatePrice(1000, 10, 29)  #T2
calculatePrice(1000, 10, 49)  #T3
#
# Invalid EC
calculatePrice(-1000, 10, 19)  #T4
# calculatePrice('rashed', 10, 29)  #T5
# calculatePrice(1000, -10, 49)  #T6
# calculatePrice(1000, 110, 49)  #T7
# calculatePrice(1000, '10', 49)  #T8
# calculatePrice(1000, 10, 20)  #T9
# calculatePrice(1000, 10, '49')  #T10


