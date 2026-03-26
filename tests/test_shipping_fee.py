import pytest
from shipping_fee import shipping_cost


def test_domestic_light_standard():
    assert shipping_cost(2, "domestic", False, False) == 5


def test_domestic_medium_standard():
    assert shipping_cost(6, "domestic", False, False) == 10


def test_international_heavy_express():
    assert shipping_cost(12, "international", True, False) == 42


def test_invalid_weight():
    with pytest.raises(ValueError):
        shipping_cost(0, "domestic", False, False)