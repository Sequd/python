# House Password
def check_password(data: str) -> bool:
    """Проверка пароля"""
    if len(data) < 10:
        return False

    digital = 0
    upper = 0
    lower = 0

    for c in data:
        if str.isdigit(c):
            digital += 1
        if str.isupper(c):
            upper += 1
        if str.islower(c):
            lower += 1

    if digital > 0 and upper > 0 and lower > 0:
        return True
    return False


def test_check_password():
    assert check_password('A1213pokl') == False
    assert check_password('bAse730onE') == True
    assert check_password('asasasasasasasaas') == False
    assert check_password('QWERTYqwerty') == False
    assert check_password('123456123456') == False
    assert check_password('QwErTy911poqqqq') == True


# test_check_password()


# The Most Wanted Letter
def most_wanted(text):
    lower = list(text.lower())
    d = {}
    for v in lower:
        if str.isalpha(v):
            if v in d:
                d[v] = d[v] + 1
            else:
                d[v] = 1

    print(d.items())
    sorted_list = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    print(sorted_list)
    print(sorted_list[0])
    key, value = sorted_list[0]
    return key


def test_most_wanted():
    assert most_wanted("Hello World!") == "l", "Hello test"
    assert most_wanted("How do you do?") == "o", "O is most wanted"
    assert most_wanted("One") == "e", "All letter only once."
    assert most_wanted("Oops!") == "o", "Don't forget about lower case."
    assert most_wanted("AAaooo!!!!") == "a", "Only letters."
    assert most_wanted("abe") == "a", "The First."
    print("Start the long test")
    assert most_wanted("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")


test_most_wanted()
