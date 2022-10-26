from Assignment2_Unit1 import two_sum
def test_normal_true():
    assert two_sum(4, [1, 2, 3, 4], 3) == (0, 1)
def test_normal_failed():
    assert two_sum(4, [1, 2, 3, 4], 9) == "None item"
def test_index1():
    assert two_sum("k", [1, 2, 3, 4], 3) == "Data type not true"
def test_index2():
    assert two_sum(-3, [1, 2, 3, 4], 3) == "Sorry, numbers below zero not alowwed"
def test_array():
    assert two_sum(4, [1, "k", 3, 4], 3) == "Data type not true"
def test_target():
    assert two_sum(4, [1, 2, 3, 4], "k") == "Type not true"