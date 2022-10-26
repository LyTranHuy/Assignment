
from Assignment1_Unit2 import replace_char

def test_method_normal():
    assert replace_char("asdasdasd", 4, "*") == "asda*dasd"

def test_method_char():
    assert replace_char("asdasdasd", "k", "y") == "Data type not true"

def test_method_minus():
    assert replace_char("asdasdasd", -5, "y") == "Sorry, no numbers below zero"

def test_method_lenght():
    assert replace_char("asdasdasd", 12, "y") == "Index is more than the length of string"