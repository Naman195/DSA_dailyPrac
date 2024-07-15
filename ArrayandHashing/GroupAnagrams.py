strs = ["eat","tea","tan","ate","nat","bat"]

from collections import defaultdict

def grpanagrams(strs):
    ans = []
    umap = defaultdict(list)
   
    for s in strs:
        sorted_str = "".join(sorted(s))
        umap[sorted_str].append(s)
    print(umap)
    
    for key in umap:
        ans.append(umap[key])
    return ans
print(grpanagrams(strs))