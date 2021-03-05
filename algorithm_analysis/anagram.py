"""One string is an anagram of the other is the second string is the rearrangement of the other."""

## solution 1: Checking off 0(n^2)
def anagram_1(s1, s2):
    a_list = list(s2)

    pos_1 = 0
    still_ok = True

    while pos_1 < len(s1) and still_ok:
        pos_2 = 0
        found = False
        while pos_2 < len(a_list) and not found:
            if s1[pos_1] == a_list[pos_2]:
                found = True
            else:
                pos_2 += 1

        if found:
             a_list[pos_2] = None
        else:
            still_ok = False

        pos_1 += 1

    return still_ok

print(anagram_1('abcd', 'dcba'))

## Solution2: Sort & Compare 0(n log n)
def anagram_2(s1, s2):
    a_list_1 = list(s1)
    a_list_2 = list(s2)

    a_list_1.sort()
    a_list_2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list_1[pos] == a_list_2[pos]:
            pos += 1
        else:
            return matches
    
    return matches

print(anagram_2('abcde', 'edcba'))

## Solution3: Count and Compare 0(n)
def anagram_3(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j += 1
        else:
            still_ok = False

    return still_ok

print(anagram_3('apple', 'pleap'))
