'''
   @pintia psid=994805260223102976 pid=994805266514558976 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1066 图像过滤
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805266514558976
   
'''

# @pintia code=start
def main():
    m, n, a, b, target = input().split()
    a = int(a)
    b = int(b)

    for i in range(m):
        row = input().split()
        for pixel in row:
            pixel = int(pixel)
            if pixel >= a and pixel <= b:
                print(0, end="", sep=" ")
        print()
        
      


main()

# @pintia code=end