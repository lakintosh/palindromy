def check_palindrome(word):
    word = word.lower()
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else: return False