def main():
    n = int(input())
    for _ in range(n):
        s = input()
        print("YES") if jusge(s) == True else print("NO")

def judge(s):
    p_index = s.find("P")
    t_index = s.find("T")
    if p_index == -1 or t_index == -1:
        return False
    left = s[ :p_index]
    middle = s[p_index: t_index]
    right = s[t_index: ]

    if len(left) * len(middle) != len(right):
        return False

    if full_a(left) == False:
        return False
    if full_a(middle) == False:
        return False
    if full_a(right) == False:
        return False
    return True

if __name__ == "__main__":
    main()


