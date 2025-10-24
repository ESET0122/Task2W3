from main import divide
def test_divide_positive_numbers() -> None:
    
    assert divide(1, 2) == 0.5


def test_divide_negative_numbers() -> None:
    
    assert divide(5, -2) == -2.5
    assert divide(-2, 5) == -0.4