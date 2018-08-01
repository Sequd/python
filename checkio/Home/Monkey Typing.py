def count_words(text: str, words: set) -> int:
    # 0 < len(text) ≤ 256
    # all(3 ≤ len(w) and w.islower() and w.isalpha for w in words)
    count = 0
    text = text.lower()
    for word in words:
        if word in text:
            count += 1
    return count


def test_count_words():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


test_count_words()
