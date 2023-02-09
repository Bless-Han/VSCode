x = 200
def main():
    global x
    x = int(input())
    my_fun2()
    my_fun()


def my_fun():
    print(x)
    

def my_fun2():
    global x
    x = 2

main()

