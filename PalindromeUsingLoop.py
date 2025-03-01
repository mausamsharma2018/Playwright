
def is_palindrome(s):
     s = s.lower()  # Convert to lowercase for case-insensitive check
     length = len(s)

     for i in range( length//2):
         if s[i] != s[length - i - 1]:
             return False
     return True

print(is_palindrome("Hannah"))
print(is_palindrome("hello"))
print(is_palindrome("Racecar"))