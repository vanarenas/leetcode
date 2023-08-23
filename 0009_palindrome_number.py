class Solution:
    def isPalindrome(self, x):
        self.x = x

        is_palindrome = False
        reversed_x = ''.join(reversed(str(self.x)))
        if str(self.x) == reversed_x:
            is_palindrome = True

        return is_palindrome


# ----- TEST CASE ----- #
x = 121
is_palindrome = Solution()
print(is_palindrome.isPalindrome(x))