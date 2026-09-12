from stock_utils.algo import binary_search

def test_find_item_in_middle():
    assert binary_search(5, [1, 3, 5, 7, 9]) == True

def test_find_item_at_left_boundary():
    assert binary_search(1, [1, 3, 5, 7, 9]) == True

def test_find_item_at_right_boundary():
    assert binary_search(9, [1, 3, 5, 7, 9]) == True

def test_item_not_in_list():
    assert binary_search(4, [1, 3, 5, 7, 9]) == False

def test_single_element_match():
    assert binary_search(1, [1]) == True

def test_single_element_no_match():
    assert binary_search(2, [1]) == False

def test_empty_list():
    assert binary_search(1, []) == False
