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
