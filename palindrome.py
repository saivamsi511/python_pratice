def palindrome(n):
    if n == n[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")
palindrome("515")