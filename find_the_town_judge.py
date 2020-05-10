class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if(N==1):
            return 1
        newTrust=list(zip(*trust))
        a=set(newTrust[1]).difference(set(newTrust[0]))
        if(len(a)!=1):
            return -1
        else:
            m=list(a)
            if(newTrust[1].count(m[0])==len(set(newTrust[0]))):
                return m[0]
            else:
                return -1