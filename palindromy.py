def check_palindrome(word):
    """
    Checks if word and reversed word are equal.
    Argument should be a string.
    :param word:
    :returns: True or False
    """
    if type(word) == str:
        word = word.lower()
        reversed_word = word[::-1]
        if word == reversed_word:
            return True
        else: return False
    else: return "Argument should be a string!"


print(check_palindrome("Krystian"))
print(check_palindrome("Zakaz"))
print(check_palindrome("kajak"))
print(check_palindrome(10))
