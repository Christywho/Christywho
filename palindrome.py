def isPalindrome(s: str) -> bool:    
    def ispalindromehelper(l, r, s):
        if l >= r:
            return True
        if s[l]!=s[r]:
            return False
        return ispalindromehelper(l+1,r-1, s)
    
    return ispalindromehelper(0, len(s)-1, s)
    
