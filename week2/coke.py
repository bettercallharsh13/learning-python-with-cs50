main_amount = 50

while main_amount > 0 :
    print("Amount Due:", main_amount)

    coin = int(input("insert coin: "))

    if coin == 25 or coin == 10 or coin == 5 :
        main_amount -= coin

print("Change Owed:", abs(main_amount))
