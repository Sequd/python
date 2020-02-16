# Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.

def is_palindrome(string):
    print(string[::-1])
    #  return string == ''.join(reversed(string))
    return string == string[::-1]


print(is_palindrome('abba'))
