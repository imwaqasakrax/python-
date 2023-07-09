class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = ""
        l1 = 0
        l2 = 0
        count = 0
        while l1 < len(word1) and l2 < len(word2):
            if count %2 ==0:
                ans =  ans+word1[l1]
                l1+=1
            elif count%2!=0:
                ans = ans+word2[l2]
                l2+=1
            count+=1
        
        if l1<len(word1):
            ans+=word1[l1:]
        if l2<len(word2):
            ans+=word2[l2:]

        return ans