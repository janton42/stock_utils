from stock_utils.algo.lexicographical_ordering import compare_strings


def test_equal_strings():
    assert compare_strings("apple", "apple") == 0

def test_s1_less_than_s2():
    assert compare_strings("apple", "banana") == -1

def test_s1_greater_than_s2():
    assert compare_strings("banana", "apple") == 1

def test_s1_prefix_of_s2():
    assert compare_strings("app", "apple") == -1

def test_s2_prefix_of_s1():
    assert compare_strings("apple", "app") == 1

def test_empty_strings_equal():
    assert compare_strings("", "") == 0

def test_empty_s1_less_than_s2():
    assert compare_strings("", "a") == -1

def test_empty_s2_greater_than_s1():
    assert compare_strings("a", "") == 1

def test_single_char_equal():
    assert compare_strings("a", "a") == 0

def test_single_char_less():
    assert compare_strings("a", "b") == -1

def test_single_char_greater():
    assert compare_strings("b", "a") == 1

def test_case_sensitive():
    # uppercase letters have lower ord values than lowercase
    assert compare_strings("A", "a") == -1
