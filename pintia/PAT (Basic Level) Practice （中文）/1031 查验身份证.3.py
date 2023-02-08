'''
   @pintia psid=994805260223102976 pid=994805290334011392 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1031 查验身份证
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805290334011392
   
'''

# @pintia code=start
weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
# in z_table, the number of "10" is as well as "X"
z_table = [1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2]

def get_z(id):
    amount = 0
    for i in range(len(id) - 1):
        amount += weight[i] * int(id[i])
    return amount % 11


# to change "X" to nubmer
def clear_m(c):
    if c == "X":
        ret = 10
    else:
        ret = int(c)
    return ret


def judge_id(id):
    try:
        z = get_z(id)
    except ValueError:
        return False
    m = z_table[z]
    if m == clear_m(id[-1]):
        return True
    return False
   

def print_people(people):
    for p in people:
      if p["judge"] == False:
         print(p["id"])

   

n = int(input())

# True, if all passed
all_passed = True

# creat a list of dictionary which like this {"id": "23123141232", "judge": False}
people = []
for i in range(n):
   temp_id = input()
   temp_judge = judge_id(temp_id)
   if temp_judge == False:
      all_passed = False
   people.append({"id":temp_id, "judge":temp_judge})

if all_passed == True:
   print("All passed")
else:
    print_people(people)


# @pintia code=end