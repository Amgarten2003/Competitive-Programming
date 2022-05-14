valor = float(input())

if (0 < valor <= 2000):
    print("Isento")

elif (2000 < valor <= 3000):
    t = valor - 2000
    tx = (t * 8) / 100
    print("R$ {:.2f}".format(tx))

elif (3000 < valor <= 4500):
    t = valor - 2000
    t1 = t - 1000
    tx1 = (1000 * 8) / 100
    tx2 = (t1 * 18) / 100
    print("R$ {:.2f}".format((tx1 + tx2)))

else:
    t = valor - 2000
    t1 = t - 1000
    tx1 = (1000 * 8) / 100
    t2 = t1 - 1500
    tx2 = (1500 * 18) / 100
    tx = (t2 * 28) / 100
    print("R$ {:.2f}".format((tx+tx1+tx2)))