for x in range(5):
    print('x: ', x)
    try: print(pow(2.71828183, x))
    except: print(None)
    try: print(1 / (x * (x - 1) * (x - 2)))
    except: print(None)
    print('---------------------')

x = 2.06
print('x: ', x)
try: print(pow(2.71828183, x))
except: print(None)
try: print(1 / (x * (x - 1) * (x - 2)))
except: print(None)
print('---------------------')
