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
    def test_randomDice():
        
    