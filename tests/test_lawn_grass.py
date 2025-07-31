def test_grass_add_returns_correct_sum(grass1, grass2):
    expected = grass1.price * grass1.quantity + grass2.price * grass2.quantity
    result = grass1 + grass2
    assert result == expected
