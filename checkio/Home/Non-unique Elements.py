# Non-unique Elements
def non_unique(data: list) -> list:
    temp = {}
    result = []

    for el in data:
        temp[el] = temp.get(el, 0) + 1

    for el in data:
        c = temp.get(el, 0)
        if c > 1:
            result.append(el)

    return result


def non_unique_2(data: list) -> list:
    return [i for i in data if data.count(i) > 1]


def test_non_unique():
    assert isinstance(non_unique([1]), list), "The result must be a list"
    assert non_unique([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert non_unique([1, 2, 3, 4, 5]) == [], "2nd example"
    assert non_unique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert non_unique([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"


test_non_unique()
