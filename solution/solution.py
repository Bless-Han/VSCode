
def change(num):
    if num == 0:
        ret_str = "0"
    else:
        ret_str = ""
    mars = "0123456789ABC"
    while num > 0:
        num, rai = divmod(num, 13)
        ret_str = mars[rai] + ret_str
    if len(ret_str) == 1:
        ret_str = "0" + ret_str
    return ret_str

r, g, b = map(int, input().split())
print(f"#{change(r)}{change(g)}{change(b)}")

