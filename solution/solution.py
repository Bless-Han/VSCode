def main():
    k = int(input())
    nums = []
    while True:
        n = int(input())
        if n < 0:
            break
        nums.append(n)
    if k > len(nums):
        print("NULL")
    else:
        print(nums[-k])

main()
