def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    max_count = 0
    last_c = ''
    count = 1
    for c in line:
        if last_c is c:
            count += 1
        else:
            count = 1
        max_count = max(count, max_count)
        last_c = c
    return max_count


def test_long_repeat():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('aa') == 2, "First1"
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')


test_long_repeat()
