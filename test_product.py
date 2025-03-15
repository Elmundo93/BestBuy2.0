import pytest
from products import Product

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