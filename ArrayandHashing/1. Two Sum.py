ar = [3,2,4]
tar = 6
# def twoSum(ar, tar):
#     for i in range(len(ar)):
#         istElInd = i
#         newTar = tar - ar[istElInd]
#         if newTar in ar:
#             return [istElInd, ar.index(newTar)]

# print(twoSum(ar, tar))
        

def twoSumm(arr, tar):
    hm = {}
    for i in range(len(arr)):
        curr = arr[i]
        newT = tar - curr
        
        if newT in hm:
            return [hm[newT], i]
        
        hm[curr] = i
    return [-1, -1]

print(twoSumm(ar, tar))        
            
            