class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        uni_char = {}
        ans = float('-inf')
        i, j = 0, 0

        while j < len(s):
            if s[j] not in uni_char:
                uni_char[s[j]] = 0
                j += 1
                ans = max(ans, len(uni_char))
            else:
                del uni_char[s[i]]
                i += 1
        ans = 0 if ans == float('-inf') else ans
        return ans
