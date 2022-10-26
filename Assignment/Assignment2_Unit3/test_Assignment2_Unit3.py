from Assignment2_Unit3 import not_duplicated
def test_normal():
    assert not_duplicated(4, ["bcdef", "abcdef", "bcde", "bcdef"]) == (3, [2, 1, 1])

def test_wrong_index_char():
    assert not_duplicated("k", ["bcdef", "abcdef", "bcde", "bcdef"]) == "Data type not true"

def test_wrong_index_negative():
    assert not_duplicated(-2, ["bcdef", "abcdef", "bcde", "bcdef"]) == "Negative not allowwed"


