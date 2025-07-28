def test_smartphone_add_returns_correct_sum(smartphone1, smartphone2):
    expected = smartphone1.price * smartphone1.quantity + smartphone2.price * smartphone2.quantity
    result = smartphone1 + smartphone2
    assert result == expected
