s = "anagram"
t = "nagaram"

def validAnagram(s, t):
    if len(s) != len(t):
        return False
    
    ar = [0]*256
    for i in range(len(s)):
        ar[ord(s[i])] += 1
        
    for i in range(len(s)):
        ar[ord(t[i])] -= 1
        
    for i in ar:
        if i > 0:
            return False
    return True

print(validAnagram(s, t))
            
    