def function(*numbers, name="world"):
    for i in numbers:
        print(i)
    print(f"hello, {name}")
        
function("1kdfj", "sldf", name="Neo")