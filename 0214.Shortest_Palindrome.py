class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        s = aacecaaa
        r = aaacecaa
            i
        result a + aacecaaa


        """
        
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s
