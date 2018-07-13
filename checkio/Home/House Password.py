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


test_check_password()
