import pytest
from products import Product
from promotions import PercentageDiscount, SecondItemHalfPrice, Buy2Get1Free

def test_create_normal_product():
    """Test that creating a product with valid details works."""
    product = Product("MacBook Air M2", 1450, 100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100

def test_create_invalid_product_empty_name():
    """Test that creating a product with an empty name raises an exception."""
    with pytest.raises(ValueError):
        Product("", 1450, 100)

def test_create_invalid_product_negative_price():
    """Test that creating a product with a negative price raises an exception."""
    with pytest.raises(ValueError):
        Product("MacBook Air M2", -10, 100)

def test_product_becomes_inactive_at_zero_quantity():
    """
    Test that when a product reaches 0 quantity it becomes inactive.
    Here we assume that a product with 0 quantity is considered inactive.
    If you add an is_active() method, you could also test:
        assert not product.is_active()
    """
    product = Product("Test Product", 10, 1)
    product.reduce_quantity(1)
    assert product.quantity == 0
    # Uncomment the following if you implement an is_active() method.
    # assert not product.is_active()

def test_product_purchase_modifies_quantity_and_returns_output():
    """Test that a valid purchase reduces the quantity and returns True."""
    product = Product("Test Product", 10, 5)
    result = product.reduce_quantity(3)
    assert result is True
    assert product.quantity == 2

def test_purchase_larger_quantity_than_exists():
    """Test that trying to buy more than the available quantity raises an exception."""
    product = Product("Test Product", 10, 2)
    with pytest.raises(ValueError):
        product.reduce_quantity(3)




def test_percentage_discount_promotion():
    """Test that a 20% percentage discount is applied correctly."""
    product = Product("Test Product", 100, 10)
    product.set_promotion(PercentageDiscount(20))
    # For 3 items, cost = 3 * 100 * 0.8 = 240
    cost = product.buy(3)
    assert cost == 240
    assert product.quantity == 7

def test_second_item_half_price_promotion():
    """Test that the 'second item at half price' promotion works correctly for even quantity."""
    product = Product("Test Product", 100, 10)
    product.set_promotion(SecondItemHalfPrice())
    # For 2 items, expected cost = 100 (first item) + 50 (half price for second) = 150
    cost = product.buy(2)
    assert cost == 150
    assert product.quantity == 8

def test_second_item_half_price_promotion_odd_quantity():
    """Test that the 'second item at half price' promotion works correctly for odd quantity."""
    product = Product("Test Product", 100, 10)
    product.set_promotion(SecondItemHalfPrice())
    # For 3 items: one pair costs 150 (as above) and one extra item costs 100.
    # Total expected = 150 + 100 = 250
    cost = product.buy(3)
    assert cost == 250
    assert product.quantity == 7

def test_buy2get1free_promotion_exact_group():
    """Test that the 'buy 2, get 1 free' promotion applies correctly when buying exactly 3 items."""
    product = Product("Test Product", 100, 10)
    product.set_promotion(Buy2Get1Free())
    # For 3 items, expected cost = price of 2 items = 2 * 100 = 200
    cost = product.buy(3)
    assert cost == 200
    assert product.quantity == 7

def test_buy2get1free_promotion_with_extra():
    """Test that the 'buy 2, get 1 free' promotion applies correctly with an extra item."""
    product = Product("Test Product", 100, 10)
    product.set_promotion(Buy2Get1Free())
    # For 4 items: one group of 3 costs 200, plus one extra item costs 100.
    # Total expected = 200 + 100 = 300
    cost = product.buy(4)
    assert cost == 300
    assert product.quantity == 6



def test_apply_promotion_directly_percentage():
    product = Product("Test Product", 100, 10)
    promotion = PercentageDiscount(20)
    cost = promotion.apply_promotion(product, 5)
    assert cost == 5 * 100 * 0.8

def test_apply_promotion_directly_second_item():
    product = Product("Test Product", 100, 10)
    promotion = SecondItemHalfPrice()
    # For 4 items: 2 pairs, each costing (100 + 50), so total should be 2 * 150 = 300
    cost = promotion.apply_promotion(product, 4)
    assert cost == 300

def test_apply_promotion_directly_buy2get1free():
    product = Product("Test Product", 100, 10)
    promotion = Buy2Get1Free()
    # For 6 items: 2 groups of 3, each costing 2 * 100, so total should be 2 * 200 = 400
    cost = promotion.apply_promotion(product, 6)
    assert cost == 400