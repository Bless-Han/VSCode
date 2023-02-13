def is_passed(s):
    if (s[0] == "a" or s[0] == "p") == false:
        return false
    # count the number of "a"
    # the index of 0 is left of "a", 2 is middle of "a", 4 is right of "a"
    count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    judge = "apata"
    judge_index = 0
    for c in s:
        try:
            while judge[judge_index] != c:
                judge_index += 1
        except indexerror:
            return false
        count[judge_index] += 1
            
    #.有问题的代码:
    return count[0] * count[2] == count[4] and count[1] != 0 and count[2] != 0 and count[3] != 0


    # 正确的代码:
    # 将代码从 != 0 改成 == 1: count[1] == 1 count[3] == 1
    # return count[0] * count[2] == count[4] and count[1] == 1 and count[2] != 0 and count[3] == 1
        
    
    
# main
n = int(input().strip())

for i in (range(n)):
    print("yes") if is_passed(input()) else print("no")
