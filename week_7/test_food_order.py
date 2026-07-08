from food_order import calculate_total

def test_order1():
    # test if total food order is equal to 30
    assert calculate_total(10, 3) == 30

def test_order2():
    # test if total food order is equal to 100
    assert calculate_total(50, 2) == 100

def test_order3():
    # test if total food order is equal to 10
    assert calculate_total(5, 2) == 10

def test_invalid_input():
    # test invalid price and invalid quantity
    assert calculate_total(-10, 2) == "invalid price"
    assert calculate_total(10, -2) == "invalid quantity"