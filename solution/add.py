def main():

    add(2, 5)

    add(4, 5)

def add(a, b):
    return a + b

def value(s):
    try:
        ret = int(s)
    except ValueError:
        raise ValueError("Enter a number")
    return ret

if __name__ == "__main__":
    main()
