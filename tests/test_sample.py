import pytest
from pyrandom2pm import randomDice
class Tests:
    @pytest.fixture
    def example_fixture(self):
        yield
    def test_sanity_check(self):
        # Making a test that always passes to make sure that there is no problem with pytest.
        expected = True
        actual = True
        assert expected == actual, "Expected True to be equal to True."
    # run multiple different test cases
    @pytest.mark.parametrize("num_dice, num_sides", [(1, 6), (2, 6), (1, 10)])
    def test_randomDice_valid_input(num_dice, num_sides):
        result = randomDice(num_dice, num_sides)
        assert isinstance(result, int)
        assert 1 <= result <= num_dice * num_sides
    def test_numDice():
        with pytest.raises(ValueError):
            randomDice()
    def test_randomDice_num_dice_invalid():
        with pytest.raises(ValueError):
            randomDice(0, 6)  # Should raise ValueError for num_dice = 0
        with pytest.raises(ValueError):
            randomDice(3, 6)  # Should raise ValueError for num_dice > 2
    def test_randomDice_invalid_num_sides():
        with pytest.raises(ValueError):
            randomDice(1, 0)

    def test_randomDice_invalid_input():
        with pytest.raises(ValueError):
            randomDice(0, 0)