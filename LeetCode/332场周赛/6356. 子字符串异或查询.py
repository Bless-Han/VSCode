class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
s = "1"
queries = [[4,5]]

ret = []
search_str = []
for v in queries:
    search_int = v[1] ^ v[0]
    search_str.append(bin(search_int)[2:])
    
for v in search_str:
    find = s.find(v)
    if find == -1:
        ret.append([find, find])
    else:
        ret.append([find, find + len(v) - 1])
        
print(ret)
# return ret
    
    