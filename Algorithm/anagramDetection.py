# T(n) = (n*(n+1))/2 => O(n^2)
def anagramSolution1(s1, s2):
    alist = list(s2)
    pos1 = 0
    while pos1 < len(s1):
        found = False
        pos2 = 0
        while pos2 < len(alist):
            if alist[pos2] == s1[pos1]:
                found = True
                alist[pos2] = None
                break
            else:
                pos2 += 1
        if not found:
            return False
        pos1 += 1
    return True

# sort and compare the same complexity as sort()
def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    pos = 0
    while pos < len(s1):
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            return False
    return True

# count and compare  O(n)
def anagramSolution3(s1, s2):
    c1 = [0]*26
    c2 = [0]*26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    while j < 26:
        if c1[j] == c2[j]:
            j += 1
        else:
            return False
    return True

print(anagramSolution3('apple', 'pleap'))
