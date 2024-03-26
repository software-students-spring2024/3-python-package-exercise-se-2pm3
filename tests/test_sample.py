import pytest
from pyrandom2pm import randomDice
from pyrandom2pm import randomNum
from pyrandom2pm import randomCoin
from pyrandom2pm import random8ball
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
    #@pytest.mark.parametrize("num_dice, num_sides", [(1, 6), (2, 6)])
    def test_randomDice_valid_input(self):
        num_dice = 2
        num_sides = 6
        result = randomDice.randomDice(num_dice, num_sides)  # Call the function with the correct parameters
        assert isinstance(result, int)
        assert 1 <= result <= num_dice * num_sides
    # def test_numDice(self):
    #     with pytest.raises(ValueError):
    #         randomDice.randomDice(None, None)
    #     with pytest.raises(ValueError):
    #         randomDice.randomDice(1, None)
    #     with pytest.raises(ValueError):
    #         randomDice.randomDice(None, 6)
    def test_randomDice_num_dice_invalid(self):
        with pytest.raises(ValueError):
            randomDice.randomDice(0, 6)  # Should raise ValueError for num_dice = 0
        with pytest.raises(ValueError):
            randomDice.randomDice(3, 6)  # Should raise ValueError for num_dice > 2
        with pytest.raises(ValueError): # Should raise ValueError when all parameters are zero
            randomDice.randomDice(0, 0)
    def test_randomDice_invalid_num_sides(self):
        with pytest.raises(ValueError):# Should raise ValueError for num_dice ==0
            randomDice.randomDice(1, 0)
        

        
    def test_randomNum_valid_input(self):
        num = 255
        result = randomNum.randomNum(num)  # Call the function with the correct parameters
        assert isinstance(result, int)
        assert 1 <= result <= num
    def test_randomNum_invalid(self):
        with pytest.raises(ValueError):
            randomNum.randomNum(-1) 
        with pytest.raises(ValueError):
            randomNum.randomNum(0)  # Should raise ValueError for num = 0
   
    def test_randomCoin_valid_input(self):
        num_flip = 255
        result = randomCoin.randomCoin(num_flip)  # Call the function with the correct parameters
        assert isinstance(result, str)
        assert result is not None
    def test_randomCoin_invalid_input(self):
        with pytest.raises(ValueError):
            randomCoin.randomCoin(0)  # Should raise ValueError for num_flip = 0
        with pytest.raises(ValueError):
            randomCoin.randomCoin(-200)  # Should raise ValueError for num_flip <0
    def test_random8ball_valid_input(self):
        strn = "Hello, World"
        result = random8ball.random8ball(strn)  # Call the function with the correct parameters
        assert isinstance(result, str)
        assert result is not None