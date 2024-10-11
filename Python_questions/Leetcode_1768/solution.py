class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        ans = ""

        for i in range(min(l1,l2)):
            ans += word1[i]
            ans += word2[i]

        ans += word1[l2:] if l1>l2 else word2[l1:]

        return ans