'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c1=Counter(s)
        for index in c1:
            if(c1[index]==1):
                return(s.index(index))
        return -1
#runtime = 64ms