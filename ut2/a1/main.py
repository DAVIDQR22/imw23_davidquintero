import sys

money = int(sys.argv[1])

if money <= 0:
    print (sys.exit('Valor no válido. Por favor, introduzca otra cantidad.'))

if money >= 50:
    fifty = money // 50
    money = money % 50
    if fifty > 1:
        print (fifty, 'billetes de 50€')
    else:
        print (fifty, 'billete de 50€')

if money >= 20:
    twenty = money //20
    money = money % 20
    if twenty > 1:
        print (twenty, 'billetes de 20€')
    else:
        print (twenty, 'billete de 20€')

if money >= 10:
    ten = money // 10
    money = money % 10
    if ten > 1:
        print (ten, 'billetes de 10€')
    else:
        print (ten, 'billete de 10€')

if money >= 5:
    five = money // 5
    money = money % 5
    if five > 1:
        print (five, 'billetes de 5€')
    else:
        print (five, 'billete de 5€')

if money >= 2:
    two = money // 2
    money = money % 2
    if two > 1:
        print (two, 'monedas de 2€')
    else:
        print (two, 'moneda de 2€')

if money >= 1:
    one = money // 1
    money = money % 1
    if one > 1:
        print (one, 'monedas de 1€')
    else:
        print (one, 'moneda de 1€')
