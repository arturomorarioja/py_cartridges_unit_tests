import pytest
from app.cartridges import calculate_discount

class TestCartridges():

    #
    # Positive testing
    #

    # Valid equivalence partitions: 5-99 and 100-MAX INTEGER
    @pytest.mark.parametrize('cartridges, discount', [
        (5, 0.0),       # Partition 5-99: lower valid boundary
        (6, 0.0),
        (47, 0.0),
        (98, 0.0),
        (99, 0.0),      # Partition 5-99: upper valid boundary
        (100, 0.2),     # Partition 100-MAX INTEGER: lower valid boundary
        (101, 0.2),
        (167, 0.2),
        (167.3, 0.2),   # Edge case: implies float to int conversion
        ("167", 0.2)    # Edge case: implies string to int conversion
    ])
    def test_cartridges_passes(self, cartridges, discount):
        assert calculate_discount(cartridges) == discount

    #
    # Negative testing
    #   

    @pytest.mark.parametrize('cartridges', [
        (0), (1), (2), (3), (4),        # Invalid equivalence partition: 0-4
        (-1), (-10), (-167)             # Edge cases
    ])
    def test_cartridges_fails(self, cartridges):
        with pytest.raises(ValueError) as error_info:
            calculate_discount(cartridges)
        assert str(error_info.value) == 'The minimum order quantity is 5.'

    # Data type-based edge cases
    @pytest.mark.parametrize('cartridges', [
        ('Hello'), ('167.3')
    ])
    def test_cartridges_wrong_data_type_fails(self, cartridges):
        with pytest.raises(ValueError) as error_info:
            calculate_discount(cartridges)
        assert str(error_info.value)[0:40] == 'invalid literal for int() with base 10: '