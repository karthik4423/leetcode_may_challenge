'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if(num==1):
            return True
        beg=1
        end=num//2
        while(beg<=end):
            mid=beg+(end-beg)//2
            #print(mid)
            sq=mid**2
            if(sq)==num:
                return True
            elif(sq)>num:
                end=mid-1
            else:
                beg=mid+1
        return(False)