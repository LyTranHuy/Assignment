from Assignment3_Unit1 import final_check
def test_normal_1():
    assert final_check("4253625879615786") == "Valid"
def test_normal_2():
    assert final_check("4424424424442444") == "Valid"
def test_normal_3():
    assert final_check("5122-2368-7954-3214") == "Valid"
def test_more_digit():
    assert final_check("42536258796157867") == "Invalid"
def test_repeat():
    assert final_check("4424444424442444") == "Invalid"
def test_separators():
    assert final_check("5122-2368-7954 - 3214") == "Invalid"
def test_non_digits():
    assert final_check("44244x4424442444") == "Invalid"
def test_start_failed():
    assert final_check("0525362587961578") == "Invalid"
